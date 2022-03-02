# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild

from pkg_resources import parse_version
import kaitaistruct
from kaitaistruct import KaitaiStruct, KaitaiStream, BytesIO


if parse_version(kaitaistruct.__version__) < parse_version('0.9'):
    raise Exception("Incompatible Kaitai Struct Python API: 0.9 or later is required, but you have %s" % (kaitaistruct.__version__))

class Pb7(KaitaiStruct):
    def __init__(self, _io, _parent=None, _root=None):
        self._io = _io
        self._parent = _parent
        self._root = _root if _root else self
        self._read()

    def _read(self):
        self.a = Pb7.BlkA(self._io, self, self._root)
        self.b = Pb7.BlkB(self._io, self, self._root)
        self.c = Pb7.BlkC(self._io, self, self._root)
        self.d = Pb7.BlkD(self._io, self, self._root)
        self.bs = Pb7.BlkBs(self._io, self, self._root)

    class BlkD(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.ht = (self._io.read_bytes(24)).decode(u"UTF-8")
            self.enc_chk_0 = Pb7.EncChk(self._io, self, self._root)
            self.ot_friendship = self._io.read_u1()
            self.unused_0 = self._io.read_bytes(6)
            self.egg_date = [None] * (3)
            for i in range(3):
                self.egg_date[i] = self._io.read_u1()

            self.met_date = [None] * (3)
            for i in range(3):
                self.met_date[i] = self._io.read_u1()

            self.rank = self._io.read_u1()
            self.egg_location = self._io.read_u2le()
            self.met_location = self._io.read_u2le()
            self.ball = self._io.read_u1()
            self.multi_0 = self._io.read_u1()
            self.multi_1 = self._io.read_u1()
            self.version = self._io.read_u1()
            self.unused_1 = self._io.read_bytes(3)
            self.language = self._io.read_u1()
            self.weight_absolute = self._io.read_bytes(4)


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
            self.ability = self._io.read_u1()
            self.multi_0 = self._io.read_u1()
            self.mark_value = self._io.read_u2le()
            self.pid = self._io.read_u4le()
            self.nature = self._io.read_u1()
            self.multi_1 = self._io.read_u1()
            self.evs = [None] * (6)
            for i in range(6):
                self.evs[i] = self._io.read_u1()

            self.avs = [None] * (6)
            for i in range(6):
                self.avs[i] = self._io.read_u1()

            self.unused_0 = self._io.read_bytes(1)
            self.multi_2 = self._io.read_u1()
            self.height_absolute = self._io.read_bytes(12)
            self.unused_1 = self._io.read_bytes(2)
            self.height_scalar = self._io.read_u1()
            self.weight_scalar = self._io.read_u1()
            self.multi_3 = self._io.read_u4le()


    class EncChk(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.enc_chk = self._io.read_bytes(2)


    class BlkBs(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.status_condition = self._io.read_u4le()
            self.stat_level = self._io.read_u1()
            self.dirt_type = self._io.read_u1()
            self.dirt_location = self._io.read_u1()
            self.unused_0 = self._io.read_bytes(1)
            self.stats = [None] * (8)
            for i in range(8):
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
            self.enc_chk_0 = Pb7.EncChk(self._io, self, self._root)
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

            self.unused_0 = self._io.read_bytes(2)
            self.multi_0 = self._io.read_u4le()


    class BlkC(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.ht = (self._io.read_bytes(24)).decode(u"UTF-8")
            self.enc_chk_0 = Pb7.EncChk(self._io, self, self._root)
            self.ht_gender = self._io.read_u1()
            self.current_handler = self._io.read_u1()
            self.unused_0 = self._io.read_bytes(14)
            self.ht_friendship = self._io.read_u1()
            self.unused_1 = self._io.read_bytes(1)
            self.ht_intensity = self._io.read_u1()
            self.ht_memory = self._io.read_u1()
            self.ht_feeling = self._io.read_u1()
            self.unused_2 = self._io.read_bytes(1)
            self.ht_textvar = self._io.read_u2le()
            self.unused3 = self._io.read_bytes(2)
            self.field_event_fatigue_0 = self._io.read_u1()
            self.field_event_fatigue_1 = self._io.read_u1()
            self.fullness = self._io.read_u1()
            self.enjoyment = self._io.read_u1()


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

        self._m_met_lvl = (self.d.multi_0 & ~128)
        return self._m_met_lvl if hasattr(self, '_m_met_lvl') else None

    @property
    def form_argument_maximum(self):
        if hasattr(self, '_m_form_argument_maximum'):
            return self._m_form_argument_maximum if hasattr(self, '_m_form_argument_maximum') else None

        self._m_form_argument_maximum = (self.form_argument >> 16)
        return self._m_form_argument_maximum if hasattr(self, '_m_form_argument_maximum') else None

    @property
    def ability_num(self):
        if hasattr(self, '_m_ability_num'):
            return self._m_ability_num if hasattr(self, '_m_ability_num') else None

        self._m_ability_num = (self.a.multi_0 & 7)
        return self._m_ability_num if hasattr(self, '_m_ability_num') else None

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
    def form_argument_elapsed(self):
        if hasattr(self, '_m_form_argument_elapsed'):
            return self._m_form_argument_elapsed if hasattr(self, '_m_form_argument_elapsed') else None

        self._m_form_argument_elapsed = (self.form_argument >> 8)
        return self._m_form_argument_elapsed if hasattr(self, '_m_form_argument_elapsed') else None

    @property
    def shiny_type(self):
        if hasattr(self, '_m_shiny_type'):
            return self._m_shiny_type if hasattr(self, '_m_shiny_type') else None

        self._m_shiny_type = ((u"Square" if self.shiny_xor == 0 else u"Star") if self.is_shiny else u"")
        return self._m_shiny_type if hasattr(self, '_m_shiny_type') else None

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
    def ability(self):
        if hasattr(self, '_m_ability'):
            return self._m_ability if hasattr(self, '_m_ability') else None

        self._m_ability = self.a.ability
        return self._m_ability if hasattr(self, '_m_ability') else None

    @property
    def form_argumant_remain(self):
        if hasattr(self, '_m_form_argumant_remain'):
            return self._m_form_argumant_remain if hasattr(self, '_m_form_argumant_remain') else None

        self._m_form_argumant_remain = self.form_argument
        return self._m_form_argumant_remain if hasattr(self, '_m_form_argumant_remain') else None

    @property
    def ht_flags(self):
        if hasattr(self, '_m_ht_flags'):
            return self._m_ht_flags if hasattr(self, '_m_ht_flags') else None

        self._m_ht_flags = self.d.multi_1
        return self._m_ht_flags if hasattr(self, '_m_ht_flags') else None

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

        self._m_shiny_xor = ((((self.a.tidsid >> 16) ^ (self.a.tidsid & 65535)) ^ (self.a.pid >> 16)) ^ (self.a.pid & 65535))
        return self._m_shiny_xor if hasattr(self, '_m_shiny_xor') else None

    @property
    def form(self):
        if hasattr(self, '_m_form'):
            return self._m_form if hasattr(self, '_m_form') else None

        self._m_form = (self.a.multi_1 >> 3)
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

        self._m_fav = (self.a.multi_0 & 8) != 0
        return self._m_fav if hasattr(self, '_m_fav') else None

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

        self._m_fateful_encounter = (self.a.multi_1 & 1) == 1
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

        self._m_gender = ((self.a.multi_1 >> 1) & 3)
        return self._m_gender if hasattr(self, '_m_gender') else None

    @property
    def form_argument(self):
        if hasattr(self, '_m_form_argument'):
            return self._m_form_argument if hasattr(self, '_m_form_argument') else None

        self._m_form_argument = self.a.multi_3
        return self._m_form_argument if hasattr(self, '_m_form_argument') else None

    @property
    def ot_gender(self):
        if hasattr(self, '_m_ot_gender'):
            return self._m_ot_gender if hasattr(self, '_m_ot_gender') else None

        self._m_ot_gender = (self.d.multi_0 >> 7)
        return self._m_ot_gender if hasattr(self, '_m_ot_gender') else None

    @property
    def ivs(self):
        if hasattr(self, '_m_ivs'):
            return self._m_ivs if hasattr(self, '_m_ivs') else None

        self._m_ivs = [(self.ivs32 & 31), ((self.ivs32 >> 5) & 31), ((self.ivs32 >> 10) & 31), ((self.ivs32 >> 15) & 31), ((self.ivs32 >> 20) & 31), ((self.ivs32 >> 25) & 31)]
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

        self._m_language = self.d.language
        return self._m_language if hasattr(self, '_m_language') else None


