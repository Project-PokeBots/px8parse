# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild

from pkg_resources import parse_version
import kaitaistruct
from kaitaistruct import KaitaiStruct, KaitaiStream, BytesIO


if parse_version(kaitaistruct.__version__) < parse_version('0.9'):
    raise Exception("Incompatible Kaitai Struct Python API: 0.9 or later is required, but you have %s" % (kaitaistruct.__version__))

class Px8(KaitaiStruct):
    def __init__(self, _io, _parent=None, _root=None):
        self._io = _io
        self._parent = _parent
        self._root = _root if _root else self
        self._read()

    def _read(self):
        self.a = Px8.BlkA(self._io, self, self._root)
        self.b = Px8.BlkB(self._io, self, self._root)
        self.c = Px8.BlkC(self._io, self, self._root)
        self.d = Px8.BlkD(self._io, self, self._root)
        self.bs = Px8.BlkBattleStats(self._io, self, self._root)

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
            self.unused_d0 = self._io.read_u1()
            self.ot_textvar = self._io.read_u2le()
            self.ot_feeling = self._io.read_u1()
            self.egg_date = [None] * (3)
            for i in range(3):
                self.egg_date[i] = self._io.read_u1()

            self.met_date = [None] * (3)
            for i in range(3):
                self.met_date[i] = self._io.read_u1()

            self.unused_d1 = self._io.read_u1()
            self.egg_location = self._io.read_u2le()
            self.met_location = self._io.read_u2le()
            self.ball = self._io.read_u1()
            self.multi_d0 = self._io.read_u1()
            self.hyper_train_flags = self._io.read_u1()
            self.move_record_flag = self._io.read_u1()
            self.unused_d2 = [None] * (13)
            for i in range(13):
                self.unused_d2[i] = self._io.read_u1()

            self.tracker = self._io.read_u8le()
            self.unused_d3 = [None] * (11)
            for i in range(11):
                self.unused_d3[i] = self._io.read_u1()



    class BlkBattleStats(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.stat_level = self._io.read_u1()
            self.unused_bs0 = self._io.read_u1()
            self.stats = [None] * (6)
            for i in range(6):
                self.stats[i] = self._io.read_u2le()

            self.unused_bs1 = self._io.read_bytes_full()


    class BlkA(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.encryption_constant = self._io.read_u4le()
            self.sanity = self._io.read_u2le()
            self.checksum = self._io.read_u2le()
            self.species = self._io.read_u2le()
            self.held_item = self._io.read_u2le()
            self.tidsid = self._io.read_u4le()
            self.exp = self._io.read_u4le()
            self.ability = self._io.read_u2le()
            self.ability_num = self._io.read_u1()
            self.unused_a0 = self._io.read_u1()
            self.mark_value = self._io.read_u2le()
            self.unused_a1 = [None] * (2)
            for i in range(2):
                self.unused_a1[i] = self._io.read_u1()

            self.pid = self._io.read_u4le()
            self.nature = self._io.read_u1()
            self.stat_nature = self._io.read_u1()
            self.multi_a0 = self._io.read_u1()
            self.unused_a3 = self._io.read_u1()
            self.form = self._io.read_u2le()
            self.evs = [None] * (6)
            for i in range(6):
                self.evs[i] = self._io.read_u1()

            self.cnts = [None] * (6)
            for i in range(6):
                self.cnts[i] = self._io.read_u1()

            self.pkrs = self._io.read_u1()
            self.unused_a4 = self._io.read_u1()
            self.ribbons = [None] * (20)
            for i in range(20):
                self.ribbons[i] = self._io.read_u1()

            self.sociability = self._io.read_u4le()
            self.unused_a5 = [None] * (4)
            for i in range(4):
                self.unused_a5[i] = self._io.read_u1()

            self.height_scalar = self._io.read_u1()
            self.weight_scalar = self._io.read_u1()
            self.unused_a6 = [None] * (6)
            for i in range(6):
                self.unused_a6[i] = self._io.read_u1()



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


    class BlkB(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.nickname = (self._io.read_bytes(24)).decode(u"UTF-8")
            self.enc_chk_0 = Px8.EncChk(self._io, self, self._root)
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
            self.ivs32_kb = self._io.read_u4le()
            self.gmax_level = self._io.read_u1()
            self.unused_b0 = [None] * (3)
            for i in range(3):
                self.unused_b0[i] = self._io.read_u1()

            self.ivs32_a = self._io.read_u4le()
            self.unk98 = self._io.read_u4le()
            self.unused_b1 = [None] * (12)
            for i in range(12):
                self.unused_b1[i] = self._io.read_u1()



    class BlkC(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.ht = (self._io.read_bytes(24)).decode(u"UTF-8")
            self.enc_chk_1 = Px8.EncChk(self._io, self, self._root)
            self.ht_gender = self._io.read_u1()
            self.ht_language = self._io.read_u1()
            self.current_handler = self._io.read_u1()
            self.unused_c0 = self._io.read_u1()
            self.ht_trainer_id = self._io.read_u2le()
            self.ht_friendship = self._io.read_u1()
            self.ht_intensity = self._io.read_u1()
            self.ht_memory = self._io.read_u1()
            self.ht_feeling = self._io.read_u1()
            self.ht_textvar = self._io.read_u2le()
            self.unused_c1 = [None] * (14)
            for i in range(14):
                self.unused_c1[i] = self._io.read_u1()

            self.fullness = self._io.read_u1()
            self.enjoyment = self._io.read_u1()
            self.version = self._io.read_u1()
            self.battle_version = self._io.read_u1()
            self.region = self._io.read_u1()
            self.console_region = self._io.read_u1()
            self.language = self._io.read_u1()
            self.unke3 = self._io.read_u1()
            self.form_argument = self._io.read_u4le()
            self.affixed_ribbon = self._io.read_u1()
            self.unused_c2 = [None] * (15)
            for i in range(15):
                self.unused_c2[i] = self._io.read_u1()



    @property
    def is_noble(self):
        if hasattr(self, '_m_is_noble'):
            return self._m_is_noble if hasattr(self, '_m_is_noble') else None

        if self.is_pla:
            self._m_is_noble = (self.a.multi_a0 & 32) != 0

        return self._m_is_noble if hasattr(self, '_m_is_noble') else None

    @property
    def is_shiny(self):
        if hasattr(self, '_m_is_shiny'):
            return self._m_is_shiny if hasattr(self, '_m_is_shiny') else None

        self._m_is_shiny = ((((self.a.tidsid >> 16) ^ (self.a.tidsid & 65535)) ^ (self.a.pid >> 16)) ^ (self.a.pid & 65535)) < 15
        return self._m_is_shiny if hasattr(self, '_m_is_shiny') else None

    @property
    def can_gigantamax(self):
        if hasattr(self, '_m_can_gigantamax'):
            return self._m_can_gigantamax if hasattr(self, '_m_can_gigantamax') else None

        if self.is_pla:
            self._m_can_gigantamax = (self.a.multi_a0 & 16) != 0

        return self._m_can_gigantamax if hasattr(self, '_m_can_gigantamax') else None

    @property
    def ivs32(self):
        if hasattr(self, '_m_ivs32'):
            return self._m_ivs32 if hasattr(self, '_m_ivs32') else None

        self._m_ivs32 = (self.b.ivs32_a if self.is_pla else self.b.ivs32_kb)
        return self._m_ivs32 if hasattr(self, '_m_ivs32') else None

    @property
    def is_alpha(self):
        if hasattr(self, '_m_is_alpha'):
            return self._m_is_alpha if hasattr(self, '_m_is_alpha') else None

        self._m_is_alpha =  (((self.a.multi_a0 & 64) != 0) and (self.is_pla)) 
        return self._m_is_alpha if hasattr(self, '_m_is_alpha') else None

    @property
    def ivs(self):
        if hasattr(self, '_m_ivs'):
            return self._m_ivs if hasattr(self, '_m_ivs') else None

        self._m_ivs = [(self.ivs32 & 31), ((self.ivs32 >> 5) & 31), ((self.ivs32 >> 10) & 31), ((self.ivs32 >> 20) & 31), ((self.ivs32 >> 25) & 31), ((self.ivs32 >> 15) & 31)]
        return self._m_ivs if hasattr(self, '_m_ivs') else None

    @property
    def is_pla(self):
        if hasattr(self, '_m_is_pla'):
            return self._m_is_pla if hasattr(self, '_m_is_pla') else None

        self._m_is_pla = len(self.bs.unused_bs1) != 2
        return self._m_is_pla if hasattr(self, '_m_is_pla') else None

    @property
    def has_nickname(self):
        if hasattr(self, '_m_has_nickname'):
            return self._m_has_nickname if hasattr(self, '_m_has_nickname') else None

        self._m_has_nickname = ((self.ivs32 >> 31) & 1) == 1
        return self._m_has_nickname if hasattr(self, '_m_has_nickname') else None


