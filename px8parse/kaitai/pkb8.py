meta:
  id: pkb8
  license: MIT
  endian: le
  encoding: UTF-8
seq:
  - id: h
    type: header
  - id: a
    type: blk_a 
  - id: b
    type: blk_b
  - id: c
    type: blk_c
  - id: d
    type: blk_d
  - id: bs
    type: blk_bs
types:
  header:
    seq:
      - id: encryption_constant
        type: u4
      - id: sanity
        type: u2
      - id: checksum
        type: u2
  blk_a:
    seq:
      - id: species
        type: u2
      - id: held_item
        type: u2
      - id: tidsid
        type: u4
      - id: exp
        type: u4
      - id: ability
        type: u2
      - id: multi_0
        type: u1
      - id: unused_0
        size: 1
      - id: mark_value
        type: u2
      - id: unused_1
        size: 2
      - id: pid
        type: u4
      - id: nature
        type: u1
      - id: stat_nature
        type: u1
      - id: multi_1
        type: u1
      - id: unused_a3
        size: 1
      - id: form
        type: u2
      - id: evs
        type: u1
        repeat: expr
        repeat-expr: 6
      - id: cnts
        type: u1
        repeat: expr
        repeat-expr: 6
      - id: multi_2
        type: u1
      - id: unused_4
        size: 1
      - id: ribbons
        size: 20
      - id: sociability
        type: u4
      - id: unused_5
        size: 4
      - id: height_scalar
        type: u1
      - id: weight_scalar
        type: u1
      - id: unused_a6
        size: 6
  blk_b:
    seq:
      - id: nickname
        type: str
        size: 24
      - id: enc_chk_0
        type: enc_chk
      - id: moves
        type: u2
        repeat: expr
        repeat-expr: 4
      - id: move_pps
        type: u1
        repeat: expr
        repeat-expr: 4
      - id: move_ppups
        type: u1
        repeat: expr
        repeat-expr: 4
      - id: relearn_moves
        type: u2
        repeat: expr
        repeat-expr: 4
      - id: stat_hpcurrent
        type: u2
      - id: multi_0
        type: u4
      - id: gmax_level
        type: u1
      - id: unused_0
        size: 3
      - id: status_condition
        type: u4
      - id: palma
        type: u4
      - id: unused_1
        size: 12
  blk_c:
    seq:
      - id: ht
        type: str
        size: 24
        encoding: UTF-8
      - id: enc_chk_1
        type: enc_chk
      - id: ht_gender
        type: u1
      - id: ht_language
        type: u1
      - id: current_handler
        type: u1
      - id: unused_0
        type: u1
      - id: ht_trainer_id
        type: u2
      - id: ht_friendship
        type: u1
      - id: ht_intensity
        type: u1
      - id: ht_memory
        type: u1
      - id: ht_feeling
        type: u1
      - id: ht_textvar
        type: u2
      - id: unused_1
        size: 14
      - id: fullness
        type: u1
      - id: enjoyment
        type: u1
      - id: version
        type: u1
      - id: battle_version
        type: u1
      - id: region
        type: u1
      - id: console_region
        type: u1
      - id: language
        type: u1
      - id: unke3
        type: u1
      - id: multi_0
        type: u4
      - id: affixed_ribbon
        type: u1
      - id: unused_2
        size: 15
  blk_d:
    seq:
      - id: ot
        type: str
        size: 26
      - id: ot_friendship
        type: u1
      - id: ot_intensity
        type: u1
      - id: ot_memory
        type: u1
      - id: unused_0
        size: 1
      - id: ot_textvar
        type: u2
      - id: ot_feeling
        type: u1
      - id: egg_date
        type: u1
        repeat: expr
        repeat-expr: 3
      - id: met_date
        type: u1
        repeat: expr
        repeat-expr: 3
      - id: unused_1
        size: 1
      - id: egg_location
        type: u2
      - id: met_location
        type: u2
      - id: ball
        type: u1
      - id: multi_0
        type: u1
      - id: multi_1
        type: u1
      - id: move_record_flag
        type: u1
      - id: unused_2
        size: 13
      - id: tracker
        type: u8
      - id: unused_3
        size: 11
  blk_bs:
    seq:
      - id: stat_level
        type: u1
      - id: unused_0
        size: 1
      - id: stats
        type: u2
        repeat: expr
        repeat-expr: 6
      - id: unused_1
        size-eos: true
  enc_chk:
    seq:
      - id: enc_chk
        size: 2
        contents: [0x0, 0x0]
instances:
  species:
    value: a.species
  ability: 
    value: a.ability
  ability_num:
    value: 'a.multi_0 & 7'
  fav:
    value: '(a.multi_0 & 8) != 0'
  can_gmax:
    value: '(a.multi_0 & 16) != 0'
  fateful_encounter:
    value: '(a.multi_1 & 1) == 1'
  flag2:
    value: '(a.multi_1 & 2) == 2'
  gender:
    value: '(a.multi_1 >> 2) & 0x3'
  language:
    value: c.language
  tidsid:
    value: a.tidsid
  shiny_xor:
    value: '(tidsid >> 16) ^ (tidsid & 0xFFFF) ^ (a.pid >> 16) ^ (a.pid & 0xFFFF)'
  is_shiny:
    value: 'shiny_xor < 15'
  shiny_type:
    value: 'is_shiny ? shiny_xor == 0 ? "Square" : "Star" : ""'
  ball:
    value: d.ball
  pkrs:
    value: a.multi_2
  pkrs_days:
    value: 'pkrs & 0xF'
  pkrs_strain:
    value: 'pkrs >> 4'
  ivs32:
    value: b.multi_0
  ivs: 
    value: '[ivs32 & 0x1F, (ivs32 >> 5) & 0x1F, (ivs32 >> 10) & 0x1F, (ivs32 >> 20) & 0x1F, (ivs32 >> 25) & 0x1F, (ivs32 >> 15) & 0x1F]'
  is_egg:
    value: '((ivs32 >> 30) & 1) == 1'
  has_nickname:
    value: '((ivs32 >> 31) & 1) == 1'
  form:
    value: a.form
  form_arg:
    value: c.multi_0
  form_arg_remain:
    value: form_arg
  form_arg_elapsed:
    value: 'form_arg >> 8'
  form_arg_max:
    value: 'form_arg >> 16'
  met_lvl:
    value: 'd.multi_0 & ~0x80'
  ot_gender:
    value: 'd.multi_0 >> 7'
  ht_flags:
    value: d.multi_1
  hts:
    value: '[((ht_flags >> 0) & 1) == 1, ((ht_flags >> 1) & 1) == 1, ((ht_flags >> 2) & 1) == 1, ((ht_flags >> 3) & 1) == 1, ((ht_flags >> 4) & 1) == 1, ((ht_flags >> 5) & 1) == 1]'
  held_item:
    value: a.held_item
  nature:
    value: a.nature
  evs:
    value: a.evs
  moves:
    value: b.moves
  ot:
    value: d.ot
  ot_lang:
    value: c.ht_language
