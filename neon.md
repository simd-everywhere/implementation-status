# Summary

TL;DR: SIMDe currently implements 5194 out of 6670 (77.87%) NEON functions.  If you don't count poly types, it's 5194 / 5692 (91.25%).

SIMDe does not currently support polynomial types, so they are excluded from this list (though separate totals are often provided to be transparent about what was skipped.  We do plan to support these types in the future.

# Functions by Architecture

| Architecture | Functions | Functions with supported types | Implemented by SIMDe | Percent implemented |
|--------------|----------:|-------------------------------:|---------------------:|--------------------:|
|        ARMv7 |      3411 |                           2984 |                 2984 |             100.00% |
|        ARMv8 |      4290 |                           3479 |                 3320 |              95.43% |
|      AArch64 |      6670 |                           5692 |                 5194 |              91.25% |

# Families

There are 390 function families in NEON (based on how we define families).  Discounting functions which use unsupported types, SIMDe has completely implemented 303 (77.69%) and partially implemented another 16 (4.10%).

## Incomplete Families

There are currently 16 incomplete families.

### cmla

SIMDe currently implements 4 of 7 (57.14%) functions.

 * [ ] vcmla_f16
 * [x] vcmla_f32
 * [ ] vcmla_f16
 * [x] vcmla_f32
 * [ ] vcmlaq_f16
 * [x] vcmlaq_f32
 * [x] vcmlaq_f64

### cmla_rot

SIMDe currently implements 12 of 21 (57.14%) functions.

 * [ ] vcmla_rot90_f16
 * [x] vcmla_rot90_f32
 * [ ] vcmla_rot180_f16
 * [x] vcmla_rot180_f32
 * [ ] vcmla_rot270_f16
 * [x] vcmla_rot270_f32
 * [ ] vcmla_rot90_f16
 * [x] vcmla_rot90_f32
 * [ ] vcmlaq_rot90_f16
 * [x] vcmlaq_rot90_f32
 * [x] vcmlaq_rot90_f64
 * [ ] vcmla_rot180_f16
 * [x] vcmla_rot180_f32
 * [ ] vcmlaq_rot180_f16
 * [x] vcmlaq_rot180_f32
 * [x] vcmlaq_rot180_f64
 * [ ] vcmla_rot270_f16
 * [x] vcmla_rot270_f32
 * [ ] vcmlaq_rot270_f16
 * [x] vcmlaq_rot270_f32
 * [x] vcmlaq_rot270_f64

### div

SIMDe currently implements 3 of 9 (33.33%) functions.

 * [x] vdiv_f32
 * [ ] vdiv_f64
 * [ ] vdiv_f16
 * [x] vdiv_f32
 * [x] vdivq_f32
 * [ ] vdiv_f64
 * [ ] vdivq_f64
 * [ ] vdiv_f16
 * [ ] vdivq_f16

### dup_lane

SIMDe currently implements 75 of 78 (96.15%) functions, not counting 24 which require currently unsupported types.

 * [x] vdup_lane_s8
 * [x] vdup_lane_s16
 * [x] vdup_lane_s32
 * [x] vdup_lane_s64
 * [x] vdup_lane_u8
 * [x] vdup_lane_u16
 * [x] vdup_lane_u32
 * [x] vdup_lane_u64
 * [x] vdup_lane_f32
 * [x] vdup_lane_f64
 * [x] vdup_laneq_s8
 * [x] vdup_laneq_s16
 * [x] vdup_laneq_s32
 * [x] vdup_laneq_s64
 * [x] vdup_laneq_u8
 * [x] vdup_laneq_u16
 * [x] vdup_laneq_u32
 * [x] vdup_laneq_u64
 * [x] vdup_laneq_f32
 * [x] vdup_laneq_f64
 * [x] vdup_lane_f16
 * [ ] vdup_laneq_f16
 * [x] vdup_lane_s8
 * [x] vdupq_lane_s8
 * [x] vdup_lane_s16
 * [x] vdupq_lane_s16
 * [x] vdup_lane_s32
 * [x] vdupq_lane_s32
 * [x] vdup_lane_s64
 * [x] vdupq_lane_s64
 * [x] vdup_lane_u8
 * [x] vdupq_lane_u8
 * [x] vdup_lane_u16
 * [x] vdupq_lane_u16
 * [x] vdup_lane_u32
 * [x] vdupq_lane_u32
 * [x] vdup_lane_u64
 * [x] vdupq_lane_u64
 * [x] vdup_lane_f32
 * [x] vdupq_lane_f32
 * [x] vdup_lane_f64
 * [x] vdupq_lane_f64
 * [x] vdup_laneq_s8
 * [x] vdupq_laneq_s8
 * [x] vdup_laneq_s16
 * [x] vdupq_laneq_s16
 * [x] vdup_laneq_s32
 * [x] vdupq_laneq_s32
 * [x] vdup_laneq_s64
 * [x] vdupq_laneq_s64
 * [x] vdup_laneq_u8
 * [x] vdupq_laneq_u8
 * [x] vdup_laneq_u16
 * [x] vdupq_laneq_u16
 * [x] vdup_laneq_u32
 * [x] vdupq_laneq_u32
 * [x] vdup_laneq_u64
 * [x] vdupq_laneq_u64
 * [x] vdup_laneq_f32
 * [x] vdupq_laneq_f32
 * [x] vdup_laneq_f64
 * [x] vdupq_laneq_f64
 * [x] vdups_lane_s32
 * [x] vdupd_lane_s64
 * [x] vdups_lane_u32
 * [x] vdupd_lane_u64
 * [x] vdups_lane_f32
 * [x] vdupd_lane_f64
 * [x] vdups_laneq_s32
 * [x] vdupd_laneq_s64
 * [x] vdups_laneq_u32
 * [x] vdupd_laneq_u64
 * [x] vdups_laneq_f32
 * [x] vdupd_laneq_f64
 * [x] vdup_lane_f16
 * [x] vdupq_lane_f16
 * [ ] vdup_laneq_f16
 * [ ] vdupq_laneq_f16

### duph_lane

SIMDe currently implements 2 of 12 (16.67%) functions, not counting 8 which require currently unsupported types.

 * [ ] vduph_lane_s16
 * [ ] vduph_lane_u16
 * [ ] vduph_laneq_s16
 * [ ] vduph_laneq_u16
 * [x] vduph_lane_f16
 * [ ] vduph_laneq_f16
 * [ ] vduph_lane_s16
 * [ ] vduph_lane_u16
 * [ ] vduph_laneq_s16
 * [ ] vduph_laneq_u16
 * [x] vduph_lane_f16
 * [ ] vduph_laneq_f16

### maxnm

SIMDe currently implements 6 of 9 (66.67%) functions.

 * [x] vmaxnm_f32
 * [x] vmaxnm_f64
 * [ ] vmaxnm_f16
 * [x] vmaxnm_f32
 * [x] vmaxnmq_f32
 * [x] vmaxnm_f64
 * [x] vmaxnmq_f64
 * [ ] vmaxnm_f16
 * [ ] vmaxnmq_f16

### maxv

SIMDe currently implements 22 of 25 (88.00%) functions.

 * [x] vmaxv_s8
 * [x] vmaxv_s16
 * [x] vmaxv_s32
 * [x] vmaxv_u8
 * [x] vmaxv_u16
 * [x] vmaxv_u32
 * [x] vmaxv_f32
 * [ ] vmaxv_f16
 * [x] vmaxv_s8
 * [x] vmaxvq_s8
 * [x] vmaxv_s16
 * [x] vmaxvq_s16
 * [x] vmaxv_s32
 * [x] vmaxvq_s32
 * [x] vmaxv_u8
 * [x] vmaxvq_u8
 * [x] vmaxv_u16
 * [x] vmaxvq_u16
 * [x] vmaxv_u32
 * [x] vmaxvq_u32
 * [x] vmaxv_f32
 * [x] vmaxvq_f32
 * [x] vmaxvq_f64
 * [ ] vmaxv_f16
 * [ ] vmaxvq_f16

### minnm

SIMDe currently implements 6 of 9 (66.67%) functions.

 * [x] vminnm_f32
 * [x] vminnm_f64
 * [ ] vminnm_f16
 * [x] vminnm_f32
 * [x] vminnmq_f32
 * [x] vminnm_f64
 * [x] vminnmq_f64
 * [ ] vminnm_f16
 * [ ] vminnmq_f16

### minv

SIMDe currently implements 22 of 25 (88.00%) functions.

 * [x] vminv_s8
 * [x] vminv_s16
 * [x] vminv_s32
 * [x] vminv_u8
 * [x] vminv_u16
 * [x] vminv_u32
 * [x] vminv_f32
 * [ ] vminv_f16
 * [x] vminv_s8
 * [x] vminvq_s8
 * [x] vminv_s16
 * [x] vminvq_s16
 * [x] vminv_s32
 * [x] vminvq_s32
 * [x] vminv_u8
 * [x] vminvq_u8
 * [x] vminv_u16
 * [x] vminvq_u16
 * [x] vminv_u32
 * [x] vminvq_u32
 * [x] vminv_f32
 * [x] vminvq_f32
 * [x] vminvq_f64
 * [ ] vminv_f16
 * [ ] vminvq_f16

### padd

SIMDe currently implements 30 of 31 (96.77%) functions.

 * [x] vpadd_s8
 * [x] vpadd_s16
 * [x] vpadd_s32
 * [x] vpadd_u8
 * [x] vpadd_u16
 * [x] vpadd_u32
 * [x] vpadd_f32
 * [x] vpadd_f16
 * [x] vpadd_s8
 * [x] vpadd_s16
 * [x] vpadd_s32
 * [x] vpadd_u8
 * [x] vpadd_u16
 * [x] vpadd_u32
 * [x] vpadd_f32
 * [x] vpaddq_s8
 * [x] vpaddq_s16
 * [x] vpaddq_s32
 * [x] vpaddq_s64
 * [x] vpaddq_u8
 * [x] vpaddq_u16
 * [x] vpaddq_u32
 * [x] vpaddq_u64
 * [x] vpaddq_f32
 * [x] vpaddq_f64
 * [x] vpaddd_s64
 * [x] vpaddd_u64
 * [x] vpadds_f32
 * [x] vpaddd_f64
 * [x] vpadd_f16
 * [ ] vpaddq_f16

### pmax

SIMDe currently implements 27 of 28 (96.43%) functions.

 * [x] vpmax_s8
 * [x] vpmax_s16
 * [x] vpmax_s32
 * [x] vpmax_u8
 * [x] vpmax_u16
 * [x] vpmax_u32
 * [x] vpmax_f32
 * [x] vpmaxqd_f64
 * [x] vpmax_f16
 * [x] vpmax_s8
 * [x] vpmax_s16
 * [x] vpmax_s32
 * [x] vpmax_u8
 * [x] vpmax_u16
 * [x] vpmax_u32
 * [x] vpmax_f32
 * [x] vpmaxq_s8
 * [x] vpmaxq_s16
 * [x] vpmaxq_s32
 * [x] vpmaxq_u8
 * [x] vpmaxq_u16
 * [x] vpmaxq_u32
 * [x] vpmaxq_f32
 * [x] vpmaxq_f64
 * [x] vpmaxs_f32
 * [x] vpmaxqd_f64
 * [x] vpmax_f16
 * [ ] vpmaxq_f16

### pmin

SIMDe currently implements 25 of 28 (89.29%) functions.

 * [x] vpmin_s8
 * [x] vpmin_s16
 * [x] vpmin_s32
 * [x] vpmin_u8
 * [x] vpmin_u16
 * [x] vpmin_u32
 * [x] vpmin_f32
 * [x] vpminqd_f64
 * [ ] vpmin_f16
 * [x] vpmin_s8
 * [x] vpmin_s16
 * [x] vpmin_s32
 * [x] vpmin_u8
 * [x] vpmin_u16
 * [x] vpmin_u32
 * [x] vpmin_f32
 * [x] vpminq_s8
 * [x] vpminq_s16
 * [x] vpminq_s32
 * [x] vpminq_u8
 * [x] vpminq_u16
 * [x] vpminq_u32
 * [x] vpminq_f32
 * [x] vpminq_f64
 * [x] vpmins_f32
 * [x] vpminqd_f64
 * [ ] vpmin_f16
 * [ ] vpminq_f16

### rnd

SIMDe currently implements 5 of 8 (62.50%) functions.

 * [x] vrnd_f32
 * [ ] vrnd_f16
 * [x] vrnd_f32
 * [x] vrndq_f32
 * [x] vrnd_f64
 * [x] vrndq_f64
 * [ ] vrnd_f16
 * [ ] vrndq_f16

### rndi

SIMDe currently implements 6 of 9 (66.67%) functions.

 * [x] vrndi_f32
 * [x] vrndi_f64
 * [ ] vrndi_f16
 * [x] vrndi_f32
 * [x] vrndiq_f32
 * [x] vrndi_f64
 * [x] vrndiq_f64
 * [ ] vrndi_f16
 * [ ] vrndiq_f16

### rndm

SIMDe currently implements 6 of 9 (66.67%) functions.

 * [x] vrndm_f32
 * [x] vrndm_f64
 * [ ] vrndm_f16
 * [x] vrndm_f32
 * [x] vrndmq_f32
 * [x] vrndm_f64
 * [x] vrndmq_f64
 * [ ] vrndm_f16
 * [ ] vrndmq_f16

### rndp

SIMDe currently implements 6 of 9 (66.67%) functions.

 * [x] vrndp_f32
 * [x] vrndp_f64
 * [ ] vrndp_f16
 * [x] vrndp_f32
 * [x] vrndpq_f32
 * [x] vrndp_f64
 * [x] vrndpq_f64
 * [ ] vrndp_f16
 * [ ] vrndpq_f16

## Unimplemented Families

There are currently 16 unimplemented families.

 * aes (8 functions)
 * bfdot (3 functions)
 * bfdot_lane (6 functions)
 * divh (2 functions)
 * dupb_lane (4 functions, plus 4 functions with unsupported types)
 * eor3 (9 functions)
 * fmlal (4 functions)
 * fmlal_high (3 functions)
 * fmlal_lane (8 functions)
 * fmlal_lane_high (6 functions)
 * fmlal_lane_low (6 functions)
 * fmlal_low (3 functions)
 * fmlsl_high (3 functions)
 * fmlsl_lane_high (6 functions)
 * fmlsl_lane_low (6 functions)
 * fmlsl_low (3 functions)
 * maxnmh (2 functions)
 * maxnmv (7 functions)
 * minnmh (2 functions)
 * minnmv (7 functions)
 * mmla (7 functions)
 * mull_high_lane (16 functions)
 * mull_high_n (8 functions)
 * mulx (11 functions)
 * mulx_lane (22 functions)
 * mulx_n (3 functions)
 * mulxh (2 functions)
 * mulxh_lane (4 functions)
 * pmaxnm (10 functions)
 * pminnm (10 functions)
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
 * qshluh_n (2 functions)
 * qshrun_high_n (6 functions)
 * qshrunh_n (2 functions)
 * rax (2 functions)
 * recp (4 functions)
 * recpsh (2 functions)
 * recpxh (2 functions)
 * rnd32x (6 functions)
 * rnd32z (6 functions)
 * rnd64x (6 functions)
 * rnd64z (6 functions)
 * rnda (9 functions)
 * rndah (2 functions)
 * rndh (2 functions)
 * rndih (2 functions)
 * rndmh (2 functions)
 * rndph (2 functions)
 * rndx (9 functions)
 * rndxh (2 functions)
 * sha1 (10 functions)
 * sha1h (2 functions)
 * sha256 (8 functions)
 * sha512 (8 functions)
 * shll_high_n (24 functions)
 * shrn_high_n (12 functions)
 * sm3 (14 functions)
 * sm4 (4 functions)
 * subhn_high (12 functions)
 * sudot_lane (6 functions)
 * usdot (3 functions)
 * usdot_lane (6 functions)

## Complete Families

SIMDe contains complete implementations of 303 functions families.

 * aba
 * abal
 * abal_high
 * abd
 * abdh
 * abdl
 * abdl_high
 * abs
 * absh
 * add (10 functions with unsupported types)
 * addh
 * addhn
 * addhn_high
 * addl
 * addl_high
 * addlv
 * addv
 * addw
 * addw_high
 * and
 * bcax
 * bic
 * bsl (9 functions with unsupported types)
 * cadd_rot
 * cage
 * cageh
 * cagt
 * cagth
 * cale
 * caleh
 * calt
 * calth
 * ceq (6 functions with unsupported types)
 * ceqh
 * ceqz (6 functions with unsupported types)
 * ceqzh
 * cge
 * cgeh
 * cgez
 * cgezh
 * cgt
 * cgth
 * cgtz
 * cgtzh
 * cle
 * cleh
 * clez
 * clezh
 * cls
 * clt
 * clth
 * cltz
 * cltzh
 * clz
 * cmla_lane
 * cmla_rot_lane
 * cnt (3 functions with unsupported types)
 * combine (8 functions with unsupported types)
 * copy_lane (24 functions with unsupported types)
 * create (8 functions with unsupported types)
 * cvt (4 functions with unsupported types)
 * cvt_high (2 functions with unsupported types)
 * cvt_low (3 functions with unsupported types)
 * cvt_n
 * cvta
 * cvtah (2 functions with unsupported types)
 * cvth (2 functions with unsupported types)
 * cvth_n
 * cvtm
 * cvtmh
 * cvtn
 * cvtnh
 * cvtp
 * cvtph
 * cvtx
 * cvtx_high
 * dot
 * dot_lane
 * dup_n (12 functions with unsupported types)
 * eor
 * ext (9 functions with unsupported types)
 * fma
 * fma_lane
 * fma_n
 * fmah
 * fmah_lane
 * fms
 * fms_lane
 * fms_n
 * fmsh
 * fmsh_lane
 * get_high (8 functions with unsupported types)
 * get_lane (12 functions with unsupported types)
 * get_low (8 functions with unsupported types)
 * hadd
 * hsub
 * ld1 (12 functions with unsupported types)
 * ld1_dup (12 functions with unsupported types)
 * ld1_lane (12 functions with unsupported types)
 * ld1_x2 (12 functions with unsupported types)
 * ld1_x3 (12 functions with unsupported types)
 * ld1_x4 (12 functions with unsupported types)
 * ld2 (12 functions with unsupported types)
 * ld2_dup (12 functions with unsupported types)
 * ld2_lane (12 functions with unsupported types)
 * ld3 (12 functions with unsupported types)
 * ld3_dup (12 functions with unsupported types)
 * ld3_lane (12 functions with unsupported types)
 * ld4 (12 functions with unsupported types)
 * ld4_dup (12 functions with unsupported types)
 * ld4_lane (12 functions with unsupported types)
 * ldr (2 functions with unsupported types)
 * max
 * maxh
 * min
 * minh
 * mla
 * mla_lane
 * mla_n
 * mlal
 * mlal_high
 * mlal_high_lane
 * mlal_high_n
 * mlal_lane
 * mlal_n
 * mls
 * mls_lane
 * mls_n
 * mlsl
 * mlsl_high
 * mlsl_high_lane
 * mlsl_high_n
 * mlsl_lane
 * mlsl_n
 * mov_n (6 functions with unsupported types)
 * movl
 * movl_high
 * movn
 * movn_high
 * mul (3 functions with unsupported types)
 * mul_lane
 * mul_n
 * mulh
 * mulh_lane
 * mull (4 functions with unsupported types)
 * mull_high (4 functions with unsupported types)
 * mull_lane
 * mull_n
 * mvn (3 functions with unsupported types)
 * neg
 * negh
 * orn
 * orr
 * padal
 * paddl
 * qabs
 * qabsh
 * qadd
 * qaddh
 * qdmlal
 * qdmlal_high
 * qdmlal_high_lane
 * qdmlal_high_n
 * qdmlal_lane
 * qdmlal_n
 * qdmlalh
 * qdmlalh_lane
 * qdmlsl
 * qdmlsl_high
 * qdmlsl_high_lane
 * qdmlsl_high_n
 * qdmlsl_lane
 * qdmlsl_n
 * qdmlslh
 * qdmlslh_lane
 * qdmulh
 * qdmulh_lane
 * qdmulh_n
 * qdmulhh
 * qdmulhh_lane
 * qdmull
 * qdmull_high
 * qdmull_high_lane
 * qdmull_high_n
 * qdmull_lane
 * qdmull_n
 * qdmullh
 * qdmullh_lane
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
 * qrshl
 * qrshlh
 * qrshrn_high_n
 * qrshrn_n
 * qrshrnh_n
 * qrshrun_high_n
 * qrshrun_n
 * qrshrunh_n
 * qshl
 * qshl_n
 * qshlh
 * qshlh_n
 * qshlu_n
 * qshrn_high_n
 * qshrn_n
 * qshrnh_n
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
 * raddhn
 * raddhn_high
 * rbit (3 functions with unsupported types)
 * recpe
 * recpeh
 * recps
 * reinterpret (316 functions with unsupported types)
 * rev16 (3 functions with unsupported types)
 * rev32 (6 functions with unsupported types)
 * rev64 (6 functions with unsupported types)
 * rhadd
 * rndn
 * rndnh
 * rshl
 * rshr_n
 * rshrn_high_n
 * rshrn_n
 * rsqrte
 * rsqrteh
 * rsqrts
 * rsqrtsh
 * rsra_n
 * rsubhn
 * rsubhn_high
 * set_lane (12 functions with unsupported types)
 * shl
 * shl_n
 * shll_n
 * shr_n
 * shrn_n
 * sli_n (9 functions with unsupported types)
 * sqadd
 * sqaddh
 * sqrt
 * sqrth
 * sra_n
 * sri_n (9 functions with unsupported types)
 * st1 (12 functions with unsupported types)
 * st1_lane (12 functions with unsupported types)
 * st1_x2 (12 functions with unsupported types)
 * st1_x3 (12 functions with unsupported types)
 * st1_x4 (12 functions with unsupported types)
 * st2 (12 functions with unsupported types)
 * st2_lane (12 functions with unsupported types)
 * st3 (12 functions with unsupported types)
 * st3_lane (12 functions with unsupported types)
 * st4 (12 functions with unsupported types)
 * st4_lane (12 functions with unsupported types)
 * str (2 functions with unsupported types)
 * sub
 * subh
 * subhn
 * subl
 * subl_high
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
 * trn (6 functions with unsupported types)
 * trn1 (7 functions with unsupported types)
 * trn2 (7 functions with unsupported types)
 * tst (6 functions with unsupported types)
 * uqadd
 * uqaddh
 * uzp (6 functions with unsupported types)
 * uzp1 (7 functions with unsupported types)
 * uzp2 (7 functions with unsupported types)
 * xar
 * zip (6 functions with unsupported types)
 * zip1 (7 functions with unsupported types)
 * zip2 (7 functions with unsupported types)
