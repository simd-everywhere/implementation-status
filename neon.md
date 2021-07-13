# Summary

TL;DR: SIMDe currently implements 3503 out of 6670 (52.52%) NEON functions.  If you don't count 16-bit floats and poly types, it's 3503 / 4969 (70.50%).

SIMDe does not currently support 16-bit floating point types or polynomial types, so they are excluded from this list (though separate totals are often provided to be transparent about what was skipped.  We do plan to support these types in the future.

# Functions by Architecture

| Architecture | Functions | Functions with supported types | Implemented by SIMDe | Percent implemented |
|--------------|----------:|-------------------------------:|---------------------:|--------------------:|
|        ARMv7 |      3411 |                           2807 |                 2322 |              82.72% |
|        ARMv8 |      4290 |                           2980 |                 2371 |              79.56% |
|      AArch64 |      6670 |                           4969 |                 3503 |              70.50% |

# Families

There are 390 function families in NEON (based on how we define families).  Discounting functions which use unsupported types, SIMDe has completely implemented 255 (65.38%) and partially implemented another 4 (1.03%).

## Incomplete Families

There are currently 4 incomplete families.

### ld1_dup

SIMDe currently implements 27 of 30 (90.00%) functions, not counting 15 which require currently unsupported types.

 * [x] vld1_dup_s8
 * [x] vld1_dup_s16
 * [x] vld1_dup_s32
 * [x] vld1_dup_s64
 * [x] vld1_dup_u8
 * [x] vld1_dup_u16
 * [x] vld1_dup_u32
 * [x] vld1_dup_u64
 * [x] vld1_dup_f32
 * [ ] vld1_dup_f64
 * [x] vld1_dup_s8
 * [x] vld1q_dup_s8
 * [x] vld1_dup_s16
 * [x] vld1q_dup_s16
 * [x] vld1_dup_s32
 * [x] vld1q_dup_s32
 * [x] vld1_dup_s64
 * [x] vld1q_dup_s64
 * [x] vld1_dup_u8
 * [x] vld1q_dup_u8
 * [x] vld1_dup_u16
 * [x] vld1q_dup_u16
 * [x] vld1_dup_u32
 * [x] vld1q_dup_u32
 * [x] vld1_dup_u64
 * [x] vld1q_dup_u64
 * [x] vld1_dup_f32
 * [x] vld1q_dup_f32
 * [ ] vld1_dup_f64
 * [ ] vld1q_dup_f64

### st2_lane

SIMDe currently implements 12 of 30 (40.00%) functions, not counting 15 which require currently unsupported types.

 * [x] vst2_lane_s8
 * [x] vst2_lane_u8
 * [x] vst2_lane_s16
 * [x] vst2_lane_s32
 * [x] vst2_lane_u16
 * [x] vst2_lane_u32
 * [ ] vst2_lane_f32
 * [ ] vst2_lane_s64
 * [ ] vst2_lane_u64
 * [ ] vst2_lane_f64
 * [x] vst2_lane_s8
 * [x] vst2_lane_u8
 * [x] vst2_lane_s16
 * [ ] vst2q_lane_s16
 * [x] vst2_lane_s32
 * [ ] vst2q_lane_s32
 * [x] vst2_lane_u16
 * [ ] vst2q_lane_u16
 * [x] vst2_lane_u32
 * [ ] vst2q_lane_u32
 * [ ] vst2_lane_f32
 * [ ] vst2q_lane_f32
 * [ ] vst2q_lane_s8
 * [ ] vst2q_lane_u8
 * [ ] vst2_lane_s64
 * [ ] vst2q_lane_s64
 * [ ] vst2_lane_u64
 * [ ] vst2q_lane_u64
 * [ ] vst2_lane_f64
 * [ ] vst2q_lane_f64

### st3_lane

SIMDe currently implements 12 of 30 (40.00%) functions, not counting 15 which require currently unsupported types.

 * [x] vst3_lane_s8
 * [x] vst3_lane_u8
 * [x] vst3_lane_s16
 * [x] vst3_lane_s32
 * [x] vst3_lane_u16
 * [x] vst3_lane_u32
 * [ ] vst3_lane_f32
 * [ ] vst3_lane_s64
 * [ ] vst3_lane_u64
 * [ ] vst3_lane_f64
 * [x] vst3_lane_s8
 * [x] vst3_lane_u8
 * [x] vst3_lane_s16
 * [ ] vst3q_lane_s16
 * [x] vst3_lane_s32
 * [ ] vst3q_lane_s32
 * [x] vst3_lane_u16
 * [ ] vst3q_lane_u16
 * [x] vst3_lane_u32
 * [ ] vst3q_lane_u32
 * [ ] vst3_lane_f32
 * [ ] vst3q_lane_f32
 * [ ] vst3q_lane_s8
 * [ ] vst3q_lane_u8
 * [ ] vst3_lane_s64
 * [ ] vst3q_lane_s64
 * [ ] vst3_lane_u64
 * [ ] vst3q_lane_u64
 * [ ] vst3_lane_f64
 * [ ] vst3q_lane_f64

### st4_lane

SIMDe currently implements 12 of 30 (40.00%) functions, not counting 15 which require currently unsupported types.

 * [x] vst4_lane_s8
 * [x] vst4_lane_u8
 * [x] vst4_lane_s16
 * [x] vst4_lane_s32
 * [x] vst4_lane_u16
 * [x] vst4_lane_u32
 * [ ] vst4_lane_f32
 * [ ] vst4_lane_s64
 * [ ] vst4_lane_u64
 * [ ] vst4_lane_f64
 * [x] vst4_lane_s8
 * [x] vst4_lane_u8
 * [x] vst4_lane_s16
 * [ ] vst4q_lane_s16
 * [x] vst4_lane_s32
 * [ ] vst4q_lane_s32
 * [x] vst4_lane_u16
 * [ ] vst4q_lane_u16
 * [x] vst4_lane_u32
 * [ ] vst4q_lane_u32
 * [ ] vst4_lane_f32
 * [ ] vst4q_lane_f32
 * [ ] vst4q_lane_s8
 * [ ] vst4q_lane_u8
 * [ ] vst4_lane_s64
 * [ ] vst4q_lane_s64
 * [ ] vst4_lane_u64
 * [ ] vst4q_lane_u64
 * [ ] vst4_lane_f64
 * [ ] vst4q_lane_f64

## Unimplemented Families

There are currently 4 unimplemented families.

 * abal (12 functions)
 * abal_high (12 functions)
 * abdl_high (12 functions)
 * addhn_high (12 functions)
 * aes (8 functions)
 * bfdot (3 functions)
 * bfdot_lane (6 functions)
 * cadd_rot (8 functions, plus 6 functions with unsupported types)
 * cale (8 functions, plus 3 functions with unsupported types)
 * calt (8 functions, plus 3 functions with unsupported types)
 * cmla_lane (6 functions, plus 8 functions with unsupported types)
 * cmla_rot_lane (18 functions, plus 24 functions with unsupported types)
 * copy_lane (60 functions, plus 24 functions with unsupported types)
 * cvt_high (4 functions, plus 6 functions with unsupported types)
 * cvt_n (32 functions, plus 12 functions with unsupported types)
 * cvta (16 functions, plus 6 functions with unsupported types)
 * cvtm (16 functions, plus 6 functions with unsupported types)
 * cvtn (16 functions, plus 6 functions with unsupported types)
 * cvtp (16 functions, plus 6 functions with unsupported types)
 * cvtx (3 functions)
 * cvtx_high (2 functions)
 * div (6 functions, plus 3 functions with unsupported types)
 * dupb_lane (4 functions, plus 4 functions with unsupported types)
 * duph_lane (8 functions, plus 12 functions with unsupported types)
 * eor3 (9 functions)
 * fmlal (4 functions)
 * fmlal_lane (8 functions)
 * fms (5 functions, plus 3 functions with unsupported types)
 * fms_lane (14 functions, plus 6 functions with unsupported types)
 * fms_n (5 functions, plus 3 functions with unsupported types)
 * ld1_x2 (30 functions, plus 15 functions with unsupported types)
 * ld1_x3 (30 functions, plus 15 functions with unsupported types)
 * ld1_x4 (30 functions, plus 15 functions with unsupported types)
 * ld2_dup (30 functions, plus 15 functions with unsupported types)
 * ld2_lane (30 functions, plus 15 functions with unsupported types)
 * ld3_dup (30 functions, plus 15 functions with unsupported types)
 * ld3_lane (30 functions, plus 15 functions with unsupported types)
 * ld4_dup (30 functions, plus 15 functions with unsupported types)
 * maxnmv (4 functions, plus 3 functions with unsupported types)
 * minnmv (4 functions, plus 3 functions with unsupported types)
 * mla_lane (30 functions)
 * mlal_high_lane (16 functions)
 * mlal_high_n (8 functions)
 * mls_lane (24 functions)
 * mlsl_high_lane (16 functions)
 * mlsl_high_n (8 functions)
 * mmla (7 functions)
 * mull_high_lane (16 functions)
 * mull_high_n (8 functions)
 * mulx (8 functions, plus 3 functions with unsupported types)
 * mulx_lane (16 functions, plus 6 functions with unsupported types)
 * pmaxnm (7 functions, plus 3 functions with unsupported types)
 * pminnm (7 functions, plus 3 functions with unsupported types)
 * qdmlal (5 functions)
 * qdmlal_high (4 functions)
 * qdmlal_high_lane (8 functions)
 * qdmlal_high_n (4 functions)
 * qdmlal_lane (10 functions)
 * qdmlal_n (4 functions)
 * qdmlalh (2 functions)
 * qdmlalh_lane (4 functions)
 * qdmlsl (5 functions)
 * qdmlsl_high (4 functions)
 * qdmlsl_high_lane (8 functions)
 * qdmlsl_high_n (4 functions)
 * qdmlsl_lane (10 functions)
 * qdmlsl_n (4 functions)
 * qdmlslh (2 functions)
 * qdmlslh_lane (4 functions)
 * qdmulhh (2 functions)
 * qdmulhh_lane (4 functions)
 * qdmull_high (4 functions)
 * qdmull_high_lane (8 functions)
 * qdmull_high_n (4 functions)
 * qdmull_lane (10 functions)
 * qdmull_n (4 functions)
 * qdmullh_lane (4 functions)
 * qmovun_high (6 functions)
 * qrdmlah (7 functions)
 * qrdmlah_lane (14 functions)
 * qrdmlahh (2 functions)
 * qrdmlahh_lane (4 functions)
 * qrdmlsh (7 functions)
 * qrdmlsh_lane (14 functions)
 * qrdmlshh (2 functions)
 * qrdmlshh_lane (4 functions)
 * qrdmulhh_lane (4 functions)
 * qrshl (30 functions)
 * qrshlh (4 functions)
 * qrshrn_high_n (12 functions)
 * qrshrnh_n (4 functions)
 * qrshrun_high_n (6 functions)
 * qrshrunh_n (2 functions)
 * qshl_n (30 functions)
 * qshlh_n (4 functions)
 * qshluh_n (2 functions)
 * qshrn_high_n (12 functions)
 * qshrnh_n (4 functions)
 * qshrun_high_n (6 functions)
 * qshrunh_n (2 functions)
 * raddhn (12 functions)
 * raddhn_high (12 functions)
 * rax (2 functions)
 * recp (4 functions)
 * rnd32x (6 functions)
 * rnd32z (6 functions)
 * rnd64x (6 functions)
 * rnd64z (6 functions)
 * rnda (6 functions, plus 3 functions with unsupported types)
 * rndx (6 functions, plus 3 functions with unsupported types)
 * rshrn_high_n (12 functions)
 * rsubhn (12 functions)
 * rsubhn_high (12 functions)
 * sha1 (10 functions)
 * sha1h (2 functions)
 * sha256 (8 functions)
 * sha512 (8 functions)
 * shll_high_n (24 functions)
 * shrn_high_n (12 functions)
 * sli_n (26 functions, plus 9 functions with unsupported types)
 * sm3 (14 functions)
 * sm4 (4 functions)
 * sqrt (6 functions, plus 3 functions with unsupported types)
 * st1_x2 (30 functions, plus 15 functions with unsupported types)
 * st1_x3 (30 functions, plus 15 functions with unsupported types)
 * st1_x4 (30 functions, plus 15 functions with unsupported types)
 * subhn_high (12 functions)
 * subl_high (12 functions)
 * sudot_lane (6 functions)
 * usdot (3 functions)
 * usdot_lane (6 functions)

## Complete Families

SIMDe contains complete implementations of 255 functions families.

 * aba
 * abd (3 functions with unsupported types)
 * abdh (2 functions with unsupported types)
 * abdl
 * abs (3 functions with unsupported types)
 * absh (2 functions with unsupported types)
 * add (13 functions with unsupported types)
 * addh (2 functions with unsupported types)
 * addhn
 * addl
 * addl_high
 * addlv
 * addv
 * addw
 * addw_high
 * and
 * bcax
 * bic
 * bsl (12 functions with unsupported types)
 * cage (3 functions with unsupported types)
 * cageh (2 functions with unsupported types)
 * cagt (3 functions with unsupported types)
 * cagth (2 functions with unsupported types)
 * caleh (2 functions with unsupported types)
 * calth (2 functions with unsupported types)
 * ceq (9 functions with unsupported types)
 * ceqh (2 functions with unsupported types)
 * ceqz (9 functions with unsupported types)
 * ceqzh (2 functions with unsupported types)
 * cge (3 functions with unsupported types)
 * cgeh (2 functions with unsupported types)
 * cgez (3 functions with unsupported types)
 * cgezh (2 functions with unsupported types)
 * cgt (3 functions with unsupported types)
 * cgth (2 functions with unsupported types)
 * cgtz (3 functions with unsupported types)
 * cgtzh (2 functions with unsupported types)
 * cle (3 functions with unsupported types)
 * cleh (2 functions with unsupported types)
 * clez (3 functions with unsupported types)
 * clezh (2 functions with unsupported types)
 * cls
 * clt (3 functions with unsupported types)
 * clth (2 functions with unsupported types)
 * cltz (3 functions with unsupported types)
 * cltzh (2 functions with unsupported types)
 * clz
 * cmla (3 functions with unsupported types)
 * cmla_rot (9 functions with unsupported types)
 * cnt (3 functions with unsupported types)
 * combine (10 functions with unsupported types)
 * create (10 functions with unsupported types)
 * cvt (20 functions with unsupported types)
 * cvt_low (3 functions with unsupported types)
 * cvtah (14 functions with unsupported types)
 * cvth (26 functions with unsupported types)
 * cvth_n (24 functions with unsupported types)
 * cvtmh (12 functions with unsupported types)
 * cvtnh (12 functions with unsupported types)
 * cvtph (12 functions with unsupported types)
 * divh (2 functions with unsupported types)
 * dot
 * dot_lane
 * dup_lane (30 functions with unsupported types)
 * dup_n (15 functions with unsupported types)
 * eor
 * ext (12 functions with unsupported types)
 * fma (3 functions with unsupported types)
 * fma_lane (6 functions with unsupported types)
 * fma_n (3 functions with unsupported types)
 * fmah (2 functions with unsupported types)
 * fmah_lane (4 functions with unsupported types)
 * fmlal_high (3 functions with unsupported types)
 * fmlal_lane_high (6 functions with unsupported types)
 * fmlal_lane_low (6 functions with unsupported types)
 * fmlal_low (3 functions with unsupported types)
 * fmlsl_high (3 functions with unsupported types)
 * fmlsl_lane_high (6 functions with unsupported types)
 * fmlsl_lane_low (6 functions with unsupported types)
 * fmlsl_low (3 functions with unsupported types)
 * fmsh (2 functions with unsupported types)
 * fmsh_lane (4 functions with unsupported types)
 * get_high (10 functions with unsupported types)
 * get_lane (15 functions with unsupported types)
 * get_low (10 functions with unsupported types)
 * hadd
 * hsub
 * ld1 (15 functions with unsupported types)
 * ld1_lane (15 functions with unsupported types)
 * ld2 (15 functions with unsupported types)
 * ld3 (15 functions with unsupported types)
 * ld4 (15 functions with unsupported types)
 * ld4_lane (15 functions with unsupported types)
 * ldr (2 functions with unsupported types)
 * max (3 functions with unsupported types)
 * maxh (2 functions with unsupported types)
 * maxnm (3 functions with unsupported types)
 * maxnmh (2 functions with unsupported types)
 * maxv (3 functions with unsupported types)
 * min (3 functions with unsupported types)
 * minh (2 functions with unsupported types)
 * minnm (3 functions with unsupported types)
 * minnmh (2 functions with unsupported types)
 * minv (3 functions with unsupported types)
 * mla
 * mla_n
 * mlal
 * mlal_high
 * mlal_lane
 * mlal_n
 * mls
 * mls_n
 * mlsl
 * mlsl_high
 * mlsl_lane
 * mlsl_n
 * mov_n (9 functions with unsupported types)
 * movl
 * movl_high
 * movn
 * movn_high
 * mul (6 functions with unsupported types)
 * mul_lane (6 functions with unsupported types)
 * mul_n (3 functions with unsupported types)
 * mulh (2 functions with unsupported types)
 * mulh_lane (4 functions with unsupported types)
 * mull (4 functions with unsupported types)
 * mull_high (4 functions with unsupported types)
 * mull_lane
 * mull_n
 * mulx_n (3 functions with unsupported types)
 * mulxh (2 functions with unsupported types)
 * mulxh_lane (4 functions with unsupported types)
 * mvn (3 functions with unsupported types)
 * neg (3 functions with unsupported types)
 * negh (2 functions with unsupported types)
 * orn
 * orr
 * padal
 * padd (3 functions with unsupported types)
 * paddl
 * pmax (3 functions with unsupported types)
 * pmin (3 functions with unsupported types)
 * qabs
 * qabsh
 * qadd
 * qaddh
 * qdmulh
 * qdmulh_lane
 * qdmulh_n
 * qdmull
 * qdmullh
 * qmovn
 * qmovn_high
 * qmovnh
 * qmovun
 * qmovunh
 * qneg
 * qnegh
 * qrdmulh
 * qrdmulh_lane
 * qrdmulh_n
 * qrdmulhh
 * qrshrn_n
 * qrshrun_n
 * qshl
 * qshlh
 * qshlu_n
 * qshrn_n
 * qshrun_n
 * qsub
 * qsubh
 * qtbl1 (3 functions with unsupported types)
 * qtbl2 (3 functions with unsupported types)
 * qtbl3 (3 functions with unsupported types)
 * qtbl4 (3 functions with unsupported types)
 * qtbx1 (3 functions with unsupported types)
 * qtbx2 (3 functions with unsupported types)
 * qtbx3 (3 functions with unsupported types)
 * qtbx4 (3 functions with unsupported types)
 * rbit (3 functions with unsupported types)
 * recpe (3 functions with unsupported types)
 * recpeh (2 functions with unsupported types)
 * recps (3 functions with unsupported types)
 * recpsh (2 functions with unsupported types)
 * recpxh (2 functions with unsupported types)
 * reinterpret (376 functions with unsupported types)
 * rev16 (3 functions with unsupported types)
 * rev32 (6 functions with unsupported types)
 * rev64 (9 functions with unsupported types)
 * rhadd
 * rnd (3 functions with unsupported types)
 * rndah (2 functions with unsupported types)
 * rndh (2 functions with unsupported types)
 * rndi (3 functions with unsupported types)
 * rndih (2 functions with unsupported types)
 * rndm (3 functions with unsupported types)
 * rndmh (2 functions with unsupported types)
 * rndn (3 functions with unsupported types)
 * rndnh (2 functions with unsupported types)
 * rndp (3 functions with unsupported types)
 * rndph (2 functions with unsupported types)
 * rndxh (2 functions with unsupported types)
 * rshl
 * rshr_n
 * rshrn_n
 * rsqrte (3 functions with unsupported types)
 * rsqrteh (2 functions with unsupported types)
 * rsqrts (3 functions with unsupported types)
 * rsqrtsh (2 functions with unsupported types)
 * rsra_n
 * set_lane (15 functions with unsupported types)
 * shl
 * shl_n
 * shll_n
 * shr_n
 * shrn_n
 * sqadd
 * sqaddh
 * sqrth (2 functions with unsupported types)
 * sra_n
 * sri_n (9 functions with unsupported types)
 * st1 (15 functions with unsupported types)
 * st1_lane (15 functions with unsupported types)
 * st2 (15 functions with unsupported types)
 * st3 (15 functions with unsupported types)
 * st4 (15 functions with unsupported types)
 * str (2 functions with unsupported types)
 * sub (3 functions with unsupported types)
 * subh (2 functions with unsupported types)
 * subhn
 * subl
 * subw
 * subw_high
 * tbl1 (2 functions with unsupported types)
 * tbl2 (2 functions with unsupported types)
 * tbl3 (2 functions with unsupported types)
 * tbl4 (2 functions with unsupported types)
 * tbx1 (2 functions with unsupported types)
 * tbx2 (2 functions with unsupported types)
 * tbx3 (2 functions with unsupported types)
 * tbx4 (2 functions with unsupported types)
 * trn (9 functions with unsupported types)
 * trn1 (10 functions with unsupported types)
 * trn2 (10 functions with unsupported types)
 * tst (6 functions with unsupported types)
 * uqadd
 * uqaddh
 * uzp (9 functions with unsupported types)
 * uzp1 (10 functions with unsupported types)
 * uzp2 (10 functions with unsupported types)
 * xar
 * zip (9 functions with unsupported types)
 * zip1 (10 functions with unsupported types)
 * zip2 (10 functions with unsupported types)
