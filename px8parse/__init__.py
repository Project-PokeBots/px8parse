from typing import Union

from .crypto import Pokecypto
from .enums import enums
from .kaitai.pkb8 import Pkb8
from .kaitai.pb7 import Pb7


class PX8:
    def __init__(self, buf: Union[bytes, str]) -> None:
        if isinstance(buf, str):
            b = bytes.fromhex(buf)
        else:
            b = buf
        self._bytes = bytearray(buf)
        
        if self._is_enc():
            self._decrypt()

        if len(self.to_bytes()) == 260:
            self._kt = Pb7.from_bytes(buf=self.to_bytes())
        elif len(self.to_bytes()) == 344:
            self._kt = Pkb8.from_bytes(buf=self.to_bytes())

        self.species = enums["forms"][self._kt.a.species][self._kt.a.form]

        if self._kt.has_nickname:
            self.nickname = self._bytes[0x58:0x72].split(b"\00\00")[0].decode("utf-8")
        else:
            self.nickname = None

        self.shiny = self._kt.shiny_type if self._kt.is_shiny else None
        self.ability = enums["ability"][self._kt.a.ability]

        if self._kt.gender not in [0, 1]:
            self.gender = None
        else:
            self.gender = enums["gender"][self._kt.gender]

        self.ot_gender = enums["gender_full"][self._kt.ot_gender]
        self.ot_lang = enums["lang"][self._kt.c.language]

        self.ball = enums["ball"][self._kt.d.ball]


        if self._kt.a.held_item != 0:
            self.item = enums["items"][self._kt.a.held_item]
        else:
            self.item = None

        self.nature = enums["natures"][self._kt.a.nature]

        self.ivs = self._kt.ivs

        self.evs = self._kt.a.evs

        self.moves = []
        for m in self._kt.b.moves:
            if m != 0:
                self.moves.append(enums["moves"][m])

        self._showdown = self._parse_showdown()

        self.sprite = enums["sprites"][self._kt.a.species][self._kt.a.form][1 if self.shiny else 0]

    def __str__(self) -> str:
        if not self._bytes:
            return "nothing to see here :c"
        return self._showdown

    def __crypt__(self, seed: int, start: int, end: int) -> None:
        i = start
        while i < end:
            seed = seed * 0x41C64E6D + 0x00006073
            self._bytes[i] ^= (seed >> 16) & 0xFF
            i += 1
            self._bytes[i] ^= (seed >> 24) & 0xFF
            i += 1

    def __cryptPKM__(self, seed: int) -> None:
        self.__crypt__(seed, 8, 0x148)
        if len(self._bytes) == 0x158:
            self.__crypt__(seed, 0x148, 0x158)

    def __shuffle__(self, sv: int) -> None:
        idx = 4 * sv
        sdata = bytearray(self._bytes[:])
        for block in range(4):
            ofs = enums["crypto"]["bp"][idx + block]
            self._bytes[8 + 0x50 * block : 8 + 0x50 * (block + 1)] = sdata[
                8 + 0x50 * ofs : 8 + 0x50 * (ofs + 1)
            ]

    def _getushort(self, offset: int) -> int:
        return int.from_bytes(self._bytes[offset : offset + 2], byteorder="little")

    def _getuint(self, offset: int) -> int:
        return int.from_bytes(self._bytes[offset : offset + 4], byteorder="little")

    def _is_enc(self) -> bool:
        return self._bytes[0x70] != 0 and self._bytes[0xC0] != 0

    def _decrypt(self) -> None:
        shuffle_order = (self.raw_ec >> 13) & 0x1F
        self.__cryptPKM__(self.raw_ec)
        self.__shuffle__(shuffle_order)

    def _parse_showdown(self) -> str:
        if self._kt.has_nickname:
            nickname = self.nickname
            species = f' ({self.species})'
        else:
            nickname = ''
            species = self.species
        if self.item:
            item = f' @ {self.item}' or ''
        else:
            item = ''
        if self.gender:
            gender = f' ({self.gender})'
        else:
            gender = ''
        Set = [f'{nickname}{species}{gender}{item}', f"Ability: {self.ability}"]
        if self.shiny:
            Set.append(f"Shiny: {self.shiny}")

        Set.append(f'Ball: {self.ball}')

        Set.append(f'OT: {self._kt.d.ot}')
        Set.append(f"TID: {str(self._kt.a.tidsid)[4:]}")
        Set.append(f"SID: {str(self._kt.a.tidsid)[:4]}")
        Set.append(f"OTGender: {self.ot_gender}")
        Set.append(f"OTLanguage: {self.ot_lang}")
        

        evs, ivs = [], []
        for i, ev in enumerate(self.evs):
            if ev != 0:
                evs.append(f'{str(ev)} {enums["ev_units"][i]}')
            if self.ivs[i] != 31:
                ivs.append(f'{str(self.ivs[i])} {enums["ev_units"][i]}')
        if len(ivs) != 0:
            Set.append(f'IVs: {" / ".join(ivs)}')
        if len(evs) != 0:
            Set.append(f'EVs: {" / ".join(evs)}')
        Set.append(f"{self.nature} Nature")
        for m in self.moves:
            Set.append(f"- {m}")
        return " \n".join(Set)

    def to_bytes(self, encrypt: bool = False) -> bytes:
        if encrypt:
            return bytes(Pokecypto(data=self._bytes).encrypt())
        else:
            return bytes(self._bytes)

    @property
    def raw_ec(self) -> int:
        return self._getuint(0x0)
