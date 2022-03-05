# MIT License
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

# This file was compiled from a KSY format file downloaded from:
# https://github.com/Project-PokeBots/kaitai_struct_formats


# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild

from pkg_resources import parse_version
import kaitaistruct
from kaitaistruct import KaitaiStruct, KaitaiStream, BytesIO


if parse_version(kaitaistruct.__version__) < parse_version('0.9'):
    raise Exception("Incompatible Kaitai Struct Python API: 0.9 or later is required, but you have %s" % (kaitaistruct.__version__))

class Pkb8(KaitaiStruct):
    def __init__(self, _io, _parent=None, _root=None):
        self._io = _io
        self._parent = _parent
        self._root = _root if _root else self
        self._read()

    def _read(self):
        self.h = Pkb8.Header(self._io, self, self._root)
        self.a = Pkb8.BlkA(self._io, self, self._root)
        self.b = Pkb8.BlkB(self._io, self, self._root)
        self.c = Pkb8.BlkC(self._io, self, self._root)
        self.d = Pkb8.BlkD(self._io, self, self._root)
        self.bs = Pkb8.BlkBs(self._io, self, self._root)

    class BlkD(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.ot = (self._io.read_bytes(26)).decode(u"UTF-8")
            self.ot_friendship = self._io.read_u1()
            self.ot_intensity = self._io.read_u1()
            self.ot_memory = self._io.read_u1()
            self.unused_0 = self._io.read_bytes(1)
            self.ot_textvar = self._io.read_u2le()
            self.ot_feeling = self._io.read_u1()
            self.egg_date = [None] * (3)
            for i in range(3):
                self.egg_date[i] = self._io.read_u1()

            self.met_date = [None] * (3)
            for i in range(3):
                self.met_date[i] = self._io.read_u1()

            self.unused_1 = self._io.read_bytes(1)
            self.egg_location = self._io.read_u2le()
            self.met_location = self._io.read_u2le()
            self.ball = self._io.read_u1()
            self.multi_0 = self._io.read_u1()
            self.multi_1 = self._io.read_u1()
            self.move_record_flag = self._io.read_u1()
            self.unused_2 = self._io.read_bytes(13)
            self.tracker = self._io.read_u8le()
            self.unused_3 = self._io.read_bytes(11)


    class BlkA(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.species = self._io.read_u2le()
            self.held_item = self._io.read_u2le()
            self.tidsid = self._io.read_u4le()
            self.exp = self._io.read_u4le()
            self.ability = self._io.read_u2le()
            self.multi_0 = self._io.read_u1()
            self.unused_0 = self._io.read_bytes(1)
            self.mark_value = self._io.read_u2le()
            self.unused_1 = self._io.read_bytes(2)
            self.pid = self._io.read_u4le()
            self.nature = self._io.read_u1()
            self.stat_nature = self._io.read_u1()
            self.multi_1 = self._io.read_u1()
            self.unused_3 = self._io.read_bytes(1)
            self.form = self._io.read_u2le()
            self.evs = [None] * (6)
            for i in range(6):
                self.evs[i] = self._io.read_u1()

            self.cnts = [None] * (6)
            for i in range(6):
                self.cnts[i] = self._io.read_u1()

            self.multi_2 = self._io.read_u1()
            self.unused_4 = self._io.read_bytes(1)
            self.ribbons = self._io.read_bytes(20)
            self.sociability = self._io.read_u4le()
            self.unused_5 = self._io.read_bytes(4)
            self.height_scalar = self._io.read_u1()
            self.weight_scalar = self._io.read_u1()
            self.height_scalar_copy = self._io.read_u1()
            self.unused_6 = self._io.read_bytes(5)


    class EncChk(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.enc_chk = self._io.read_bytes(2)
            if not self.enc_chk == b"\x00\x00":
                raise kaitaistruct.ValidationNotEqualError(b"\x00\x00", self.enc_chk, self._io, u"/types/enc_chk/seq/0")


    class BlkBs(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.stat_level = self._io.read_u1()
            self.unused_0 = self._io.read_bytes(1)
            self.stats = [None] * (6)
            for i in range(6):
                self.stats[i] = self._io.read_u2le()

            self.unused_1 = self._io.read_bytes_full()


    class BlkB(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.nickname = (self._io.read_bytes(24)).decode(u"UTF-8")
            self.enc_chk_0 = Pkb8.EncChk(self._io, self, self._root)
            self.moves = [None] * (4)
            for i in range(4):
                self.moves[i] = self._io.read_u2le()

            self.move_pps = [None] * (4)
            for i in range(4):
                self.move_pps[i] = self._io.read_u1()

            self.move_ppups = [None] * (4)
            for i in range(4):
                self.move_ppups[i] = self._io.read_u1()

            self.relearn_moves = [None] * (4)
            for i in range(4):
                self.relearn_moves[i] = self._io.read_u2le()

            self.stat_hpcurrent = self._io.read_u2le()
            self.multi_0 = self._io.read_u4le()
            self.gmax_level = self._io.read_u1()
            self.unused_0 = self._io.read_bytes(3)
            self.status_condition = self._io.read_u4le()
            self.palma = self._io.read_u4le()
            self.unused_1 = self._io.read_bytes(12)


    class Header(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.encryption_constant = self._io.read_u4le()
            self.sanity = self._io.read_u2le()
            self.checksum = self._io.read_u2le()


    class BlkC(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.ht = (self._io.read_bytes(24)).decode(u"UTF-8")
            self.enc_chk_1 = Pkb8.EncChk(self._io, self, self._root)
            self.ht_gender = self._io.read_u1()
            self.ht_language = self._io.read_u1()
            self.current_handler = self._io.read_u1()
            self.unused_0 = self._io.read_u1()
            self.ht_trainer_id = self._io.read_u2le()
            self.ht_friendship = self._io.read_u1()
            self.ht_intensity = self._io.read_u1()
            self.ht_memory = self._io.read_u1()
            self.ht_feeling = self._io.read_u1()
            self.ht_textvar = self._io.read_u2le()
            self.unused_1 = self._io.read_bytes(14)
            self.fullness = self._io.read_u1()
            self.enjoyment = self._io.read_u1()
            self.version = self._io.read_u1()
            self.battle_version = self._io.read_u1()
            self.region = self._io.read_u1()
            self.console_region = self._io.read_u1()
            self.language = self._io.read_u1()
            self.unke3 = self._io.read_u1()
            self.multi_0 = self._io.read_u4le()
            self.affixed_ribbon = self._io.read_u1()
            self.unused_2 = self._io.read_bytes(15)


    @property
    def pkrs(self):
        if hasattr(self, '_m_pkrs'):
            return self._m_pkrs if hasattr(self, '_m_pkrs') else None

        self._m_pkrs = self.a.multi_2
        return self._m_pkrs if hasattr(self, '_m_pkrs') else None

    @property
    def is_shiny(self):
        if hasattr(self, '_m_is_shiny'):
            return self._m_is_shiny if hasattr(self, '_m_is_shiny') else None

        self._m_is_shiny = self.shiny_xor < 15
        return self._m_is_shiny if hasattr(self, '_m_is_shiny') else None

    @property
    def met_lvl(self):
        if hasattr(self, '_m_met_lvl'):
            return self._m_met_lvl if hasattr(self, '_m_met_lvl') else None

        self._m_met_lvl = (self.multi_d0 & ~128)
        return self._m_met_lvl if hasattr(self, '_m_met_lvl') else None

    @property
    def pid(self):
        if hasattr(self, '_m_pid'):
            return self._m_pid if hasattr(self, '_m_pid') else None

        self._m_pid = self.a.pid
        return self._m_pid if hasattr(self, '_m_pid') else None

    @property
    def ability_num(self):
        if hasattr(self, '_m_ability_num'):
            return self._m_ability_num if hasattr(self, '_m_ability_num') else None

        self._m_ability_num = (self.multi_a0 & 7)
        return self._m_ability_num if hasattr(self, '_m_ability_num') else None

    @property
    def ot_lang(self):
        if hasattr(self, '_m_ot_lang'):
            return self._m_ot_lang if hasattr(self, '_m_ot_lang') else None

        self._m_ot_lang = self.c.ht_language
        return self._m_ot_lang if hasattr(self, '_m_ot_lang') else None

    @property
    def pkrs_days(self):
        if hasattr(self, '_m_pkrs_days'):
            return self._m_pkrs_days if hasattr(self, '_m_pkrs_days') else None

        self._m_pkrs_days = (self.pkrs & 15)
        return self._m_pkrs_days if hasattr(self, '_m_pkrs_days') else None

    @property
    def hts(self):
        if hasattr(self, '_m_hts'):
            return self._m_hts if hasattr(self, '_m_hts') else None

        self._m_hts = [((self.ht_flags >> 0) & 1) == 1, ((self.ht_flags >> 1) & 1) == 1, ((self.ht_flags >> 2) & 1) == 1, ((self.ht_flags >> 3) & 1) == 1, ((self.ht_flags >> 4) & 1) == 1, ((self.ht_flags >> 5) & 1) == 1]
        return self._m_hts if hasattr(self, '_m_hts') else None

    @property
    def ot(self):
        if hasattr(self, '_m_ot'):
            return self._m_ot if hasattr(self, '_m_ot') else None

        self._m_ot = self.d.ot
        return self._m_ot if hasattr(self, '_m_ot') else None

    @property
    def shiny_type(self):
        if hasattr(self, '_m_shiny_type'):
            return self._m_shiny_type if hasattr(self, '_m_shiny_type') else None

        self._m_shiny_type = ((u"Square" if self.shiny_xor == 0 else u"Star") if self.is_shiny else u"")
        return self._m_shiny_type if hasattr(self, '_m_shiny_type') else None

    @property
    def tidsid(self):
        if hasattr(self, '_m_tidsid'):
            return self._m_tidsid if hasattr(self, '_m_tidsid') else None

        self._m_tidsid = self.a.tidsid
        return self._m_tidsid if hasattr(self, '_m_tidsid') else None

    @property
    def pkrs_strain(self):
        if hasattr(self, '_m_pkrs_strain'):
            return self._m_pkrs_strain if hasattr(self, '_m_pkrs_strain') else None

        self._m_pkrs_strain = (self.pkrs >> 4)
        return self._m_pkrs_strain if hasattr(self, '_m_pkrs_strain') else None

    @property
    def held_item(self):
        if hasattr(self, '_m_held_item'):
            return self._m_held_item if hasattr(self, '_m_held_item') else None

        self._m_held_item = self.a.held_item
        return self._m_held_item if hasattr(self, '_m_held_item') else None

    @property
    def multi_a1(self):
        if hasattr(self, '_m_multi_a1'):
            return self._m_multi_a1 if hasattr(self, '_m_multi_a1') else None

        self._m_multi_a1 = self.a.multi_1
        return self._m_multi_a1 if hasattr(self, '_m_multi_a1') else None

    @property
    def multi_d0(self):
        if hasattr(self, '_m_multi_d0'):
            return self._m_multi_d0 if hasattr(self, '_m_multi_d0') else None

        self._m_multi_d0 = self.d.multi_0
        return self._m_multi_d0 if hasattr(self, '_m_multi_d0') else None

    @property
    def flag2(self):
        if hasattr(self, '_m_flag2'):
            return self._m_flag2 if hasattr(self, '_m_flag2') else None

        self._m_flag2 = (self.multi_a1 & 2) == 2
        return self._m_flag2 if hasattr(self, '_m_flag2') else None

    @property
    def ability(self):
        if hasattr(self, '_m_ability'):
            return self._m_ability if hasattr(self, '_m_ability') else None

        self._m_ability = self.a.ability
        return self._m_ability if hasattr(self, '_m_ability') else None

    @property
    def form_arg(self):
        if hasattr(self, '_m_form_arg'):
            return self._m_form_arg if hasattr(self, '_m_form_arg') else None

        self._m_form_arg = self.c.multi_0
        return self._m_form_arg if hasattr(self, '_m_form_arg') else None

    @property
    def ht_flags(self):
        if hasattr(self, '_m_ht_flags'):
            return self._m_ht_flags if hasattr(self, '_m_ht_flags') else None

        self._m_ht_flags = self.d.multi_1
        return self._m_ht_flags if hasattr(self, '_m_ht_flags') else None

    @property
    def form_arg_max(self):
        if hasattr(self, '_m_form_arg_max'):
            return self._m_form_arg_max if hasattr(self, '_m_form_arg_max') else None

        self._m_form_arg_max = (self.form_arg >> 16)
        return self._m_form_arg_max if hasattr(self, '_m_form_arg_max') else None

    @property
    def species(self):
        if hasattr(self, '_m_species'):
            return self._m_species if hasattr(self, '_m_species') else None

        self._m_species = self.a.species
        return self._m_species if hasattr(self, '_m_species') else None

    @property
    def moves(self):
        if hasattr(self, '_m_moves'):
            return self._m_moves if hasattr(self, '_m_moves') else None

        self._m_moves = self.b.moves
        return self._m_moves if hasattr(self, '_m_moves') else None

    @property
    def shiny_xor(self):
        if hasattr(self, '_m_shiny_xor'):
            return self._m_shiny_xor if hasattr(self, '_m_shiny_xor') else None

        self._m_shiny_xor = ((((self.tidsid >> 16) ^ (self.tidsid & 65535)) ^ (self.pid >> 16)) ^ (self.pid & 65535))
        return self._m_shiny_xor if hasattr(self, '_m_shiny_xor') else None

    @property
    def form(self):
        if hasattr(self, '_m_form'):
            return self._m_form if hasattr(self, '_m_form') else None

        self._m_form = self.a.form
        return self._m_form if hasattr(self, '_m_form') else None

    @property
    def is_egg(self):
        if hasattr(self, '_m_is_egg'):
            return self._m_is_egg if hasattr(self, '_m_is_egg') else None

        self._m_is_egg = ((self.ivs32 >> 30) & 1) == 1
        return self._m_is_egg if hasattr(self, '_m_is_egg') else None

    @property
    def fav(self):
        if hasattr(self, '_m_fav'):
            return self._m_fav if hasattr(self, '_m_fav') else None

        self._m_fav = (self.multi_a0 & 8) != 0
        return self._m_fav if hasattr(self, '_m_fav') else None

    @property
    def form_arg_elapsed(self):
        if hasattr(self, '_m_form_arg_elapsed'):
            return self._m_form_arg_elapsed if hasattr(self, '_m_form_arg_elapsed') else None

        self._m_form_arg_elapsed = (self.form_arg >> 8)
        return self._m_form_arg_elapsed if hasattr(self, '_m_form_arg_elapsed') else None

    @property
    def multi_a0(self):
        if hasattr(self, '_m_multi_a0'):
            return self._m_multi_a0 if hasattr(self, '_m_multi_a0') else None

        self._m_multi_a0 = self.a.multi_0
        return self._m_multi_a0 if hasattr(self, '_m_multi_a0') else None

    @property
    def form_arg_remain(self):
        if hasattr(self, '_m_form_arg_remain'):
            return self._m_form_arg_remain if hasattr(self, '_m_form_arg_remain') else None

        self._m_form_arg_remain = self.form_arg
        return self._m_form_arg_remain if hasattr(self, '_m_form_arg_remain') else None

    @property
    def ball(self):
        if hasattr(self, '_m_ball'):
            return self._m_ball if hasattr(self, '_m_ball') else None

        self._m_ball = self.d.ball
        return self._m_ball if hasattr(self, '_m_ball') else None

    @property
    def evs(self):
        if hasattr(self, '_m_evs'):
            return self._m_evs if hasattr(self, '_m_evs') else None

        self._m_evs = self.a.evs
        return self._m_evs if hasattr(self, '_m_evs') else None

    @property
    def fateful_encounter(self):
        if hasattr(self, '_m_fateful_encounter'):
            return self._m_fateful_encounter if hasattr(self, '_m_fateful_encounter') else None

        self._m_fateful_encounter = (self.multi_a1 & 1) == 1
        return self._m_fateful_encounter if hasattr(self, '_m_fateful_encounter') else None

    @property
    def ivs32(self):
        if hasattr(self, '_m_ivs32'):
            return self._m_ivs32 if hasattr(self, '_m_ivs32') else None

        self._m_ivs32 = self.b.multi_0
        return self._m_ivs32 if hasattr(self, '_m_ivs32') else None

    @property
    def gender(self):
        if hasattr(self, '_m_gender'):
            return self._m_gender if hasattr(self, '_m_gender') else None

        self._m_gender = ((self.multi_a1 >> 2) & 3)
        return self._m_gender if hasattr(self, '_m_gender') else None

    @property
    def ot_gender(self):
        if hasattr(self, '_m_ot_gender'):
            return self._m_ot_gender if hasattr(self, '_m_ot_gender') else None

        self._m_ot_gender = (self.multi_d0 >> 7)
        return self._m_ot_gender if hasattr(self, '_m_ot_gender') else None

    @property
    def can_gmax(self):
        if hasattr(self, '_m_can_gmax'):
            return self._m_can_gmax if hasattr(self, '_m_can_gmax') else None

        self._m_can_gmax = (self.multi_a0 & 16) != 0
        return self._m_can_gmax if hasattr(self, '_m_can_gmax') else None

    @property
    def ivs(self):
        if hasattr(self, '_m_ivs'):
            return self._m_ivs if hasattr(self, '_m_ivs') else None

        self._m_ivs = [(self.ivs32 & 31), ((self.ivs32 >> 5) & 31), ((self.ivs32 >> 10) & 31), ((self.ivs32 >> 20) & 31), ((self.ivs32 >> 25) & 31), ((self.ivs32 >> 15) & 31)]
        return self._m_ivs if hasattr(self, '_m_ivs') else None

    @property
    def nature(self):
        if hasattr(self, '_m_nature'):
            return self._m_nature if hasattr(self, '_m_nature') else None

        self._m_nature = self.a.nature
        return self._m_nature if hasattr(self, '_m_nature') else None

    @property
    def has_nickname(self):
        if hasattr(self, '_m_has_nickname'):
            return self._m_has_nickname if hasattr(self, '_m_has_nickname') else None

        self._m_has_nickname = ((self.ivs32 >> 31) & 1) == 1
        return self._m_has_nickname if hasattr(self, '_m_has_nickname') else None

    @property
    def language(self):
        if hasattr(self, '_m_language'):
            return self._m_language if hasattr(self, '_m_language') else None

        self._m_language = self.c.language
        return self._m_language if hasattr(self, '_m_language') else None


