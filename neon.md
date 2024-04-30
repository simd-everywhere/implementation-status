# Summary

TL;DR: SIMDe currently implements 6608 out of 6670 (99.07%) NEON functions.

# Functions by Architecture

| Architecture | Functions | Implemented by SIMDe | Percent implemented |
|--------------|----------:|---------------------:|--------------------:|
|        ARMv7 |      3411 |                 3411 |             100.00% |
|        ARMv8 |      4290 |                 4258 |              99.25% |
|      AArch64 |      6670 |                 6608 |              99.07% |

# Families

There are 390 function families in NEON (based on how we define families).  SIMDe has completely implemented 378 (96.92%) and partially implemented another 12 (3.08%).

## Incomplete Families

There are currently 12 incomplete families.

### cvt

SIMDe currently implements 53 of 56 (94.64%) functions.

 * [x] vcvt_s32_f32
 * [x] vcvt_u32_f32
 * [x] vcvt_s64_f64
 * [x] vcvt_u64_f64
 * [x] vcvt_f32_s32
 * [x] vcvt_f32_u32
 * [x] vcvt_f64_s64
 * [x] vcvt_f64_u64
 * [x] vcvt_f16_f32
 * [x] vcvt_f32_f64
 * [x] vcvt_f32_f16
 * [x] vcvt_f64_f32
 * [x] vcvt_f16_s16
 * [x] vcvt_f16_u16
 * [ ] vcvt_s16_f16
 * [x] vcvt_u16_f16
 * [x] vcvt_f32_bf16
 * [x] vcvt_bf16_f32
 * [x] vcvt_s32_f32
 * [x] vcvtq_s32_f32
 * [x] vcvt_u32_f32
 * [x] vcvtq_u32_f32
 * [x] vcvts_s32_f32
 * [x] vcvts_u32_f32
 * [x] vcvt_s64_f64
 * [x] vcvtq_s64_f64
 * [x] vcvt_u64_f64
 * [x] vcvtq_u64_f64
 * [x] vcvtd_s64_f64
 * [x] vcvtd_u64_f64
 * [x] vcvt_f32_s32
 * [x] vcvtq_f32_s32
 * [x] vcvt_f32_u32
 * [x] vcvtq_f32_u32
 * [x] vcvts_f32_s32
 * [x] vcvts_f32_u32
 * [x] vcvt_f64_s64
 * [x] vcvtq_f64_s64
 * [x] vcvt_f64_u64
 * [x] vcvtq_f64_u64
 * [x] vcvtd_f64_s64
 * [x] vcvtd_f64_u64
 * [x] vcvt_f16_f32
 * [x] vcvt_f32_f64
 * [x] vcvt_f32_f16
 * [x] vcvt_f64_f32
 * [x] vcvt_f16_s16
 * [x] vcvtq_f16_s16
 * [x] vcvt_f16_u16
 * [x] vcvtq_f16_u16
 * [ ] vcvt_s16_f16
 * [ ] vcvtq_s16_f16
 * [x] vcvt_u16_f16
 * [x] vcvtq_u16_f16
 * [x] vcvt_f32_bf16
 * [x] vcvt_bf16_f32

### cvt_n

SIMDe currently implements 41 of 44 (93.18%) functions.

 * [x] vcvt_n_s32_f32
 * [x] vcvt_n_u32_f32
 * [x] vcvt_n_s64_f64
 * [x] vcvt_n_u64_f64
 * [x] vcvt_n_f32_s32
 * [x] vcvt_n_f32_u32
 * [x] vcvt_n_f64_s64
 * [x] vcvt_n_f64_u64
 * [x] vcvt_n_f16_s16
 * [x] vcvt_n_f16_u16
 * [ ] vcvt_n_s16_f16
 * [x] vcvt_n_u16_f16
 * [x] vcvt_n_s32_f32
 * [x] vcvtq_n_s32_f32
 * [x] vcvt_n_u32_f32
 * [x] vcvtq_n_u32_f32
 * [x] vcvts_n_s32_f32
 * [x] vcvts_n_u32_f32
 * [x] vcvt_n_s64_f64
 * [x] vcvtq_n_s64_f64
 * [x] vcvt_n_u64_f64
 * [x] vcvtq_n_u64_f64
 * [x] vcvtd_n_s64_f64
 * [x] vcvtd_n_u64_f64
 * [x] vcvt_n_f32_s32
 * [x] vcvtq_n_f32_s32
 * [x] vcvt_n_f32_u32
 * [x] vcvtq_n_f32_u32
 * [x] vcvts_n_f32_s32
 * [x] vcvts_n_f32_u32
 * [x] vcvt_n_f64_s64
 * [x] vcvtq_n_f64_s64
 * [x] vcvt_n_f64_u64
 * [x] vcvtq_n_f64_u64
 * [x] vcvtd_n_f64_s64
 * [x] vcvtd_n_f64_u64
 * [x] vcvt_n_f16_s16
 * [x] vcvtq_n_f16_s16
 * [x] vcvt_n_f16_u16
 * [x] vcvtq_n_f16_u16
 * [ ] vcvt_n_s16_f16
 * [ ] vcvtq_n_s16_f16
 * [x] vcvt_n_u16_f16
 * [x] vcvtq_n_u16_f16

### cvta

SIMDe currently implements 19 of 22 (86.36%) functions.

 * [x] vcvta_s32_f32
 * [x] vcvta_u32_f32
 * [x] vcvta_s64_f64
 * [x] vcvta_u64_f64
 * [ ] vcvta_s16_f16
 * [x] vcvta_u16_f16
 * [x] vcvta_s32_f32
 * [x] vcvtaq_s32_f32
 * [x] vcvta_u32_f32
 * [x] vcvtaq_u32_f32
 * [x] vcvtas_s32_f32
 * [x] vcvtas_u32_f32
 * [x] vcvta_s64_f64
 * [x] vcvtaq_s64_f64
 * [x] vcvta_u64_f64
 * [x] vcvtaq_u64_f64
 * [x] vcvtad_s64_f64
 * [x] vcvtad_u64_f64
 * [ ] vcvta_s16_f16
 * [ ] vcvtaq_s16_f16
 * [x] vcvta_u16_f16
 * [x] vcvtaq_u16_f16

### cvtah

SIMDe currently implements 12 of 14 (85.71%) functions.

 * [ ] vcvtah_s16_f16
 * [x] vcvtah_s32_f16
 * [x] vcvtah_s64_f16
 * [x] vcvtah_u16_f16
 * [x] vcvtah_u32_f16
 * [x] vcvtah_u64_f16
 * [x] vcvtah_f32_bf16
 * [ ] vcvtah_s16_f16
 * [x] vcvtah_s32_f16
 * [x] vcvtah_s64_f16
 * [x] vcvtah_u16_f16
 * [x] vcvtah_u32_f16
 * [x] vcvtah_u64_f16
 * [x] vcvtah_f32_bf16

### cvth

SIMDe currently implements 24 of 26 (92.31%) functions.

 * [x] vcvth_f16_s16
 * [x] vcvth_f16_s32
 * [x] vcvth_f16_s64
 * [x] vcvth_f16_u16
 * [x] vcvth_f16_u32
 * [x] vcvth_f16_u64
 * [ ] vcvth_s16_f16
 * [x] vcvth_s32_f16
 * [x] vcvth_s64_f16
 * [x] vcvth_u16_f16
 * [x] vcvth_u32_f16
 * [x] vcvth_u64_f16
 * [x] vcvth_bf16_f32
 * [x] vcvth_f16_s16
 * [x] vcvth_f16_s32
 * [x] vcvth_f16_s64
 * [x] vcvth_f16_u16
 * [x] vcvth_f16_u32
 * [x] vcvth_f16_u64
 * [ ] vcvth_s16_f16
 * [x] vcvth_s32_f16
 * [x] vcvth_s64_f16
 * [x] vcvth_u16_f16
 * [x] vcvth_u32_f16
 * [x] vcvth_u64_f16
 * [x] vcvth_bf16_f32

### cvth_n

SIMDe currently implements 6 of 24 (25.00%) functions.

 * [x] vcvth_n_f16_s16
 * [ ] vcvth_n_f16_s32
 * [ ] vcvth_n_f16_s64
 * [x] vcvth_n_f16_u16
 * [ ] vcvth_n_f16_u32
 * [ ] vcvth_n_f16_u64
 * [ ] vcvth_n_s16_f16
 * [ ] vcvth_n_s32_f16
 * [ ] vcvth_n_s64_f16
 * [x] vcvth_n_u16_f16
 * [ ] vcvth_n_u32_f16
 * [ ] vcvth_n_u64_f16
 * [x] vcvth_n_f16_s16
 * [ ] vcvth_n_f16_s32
 * [ ] vcvth_n_f16_s64
 * [x] vcvth_n_f16_u16
 * [ ] vcvth_n_f16_u32
 * [ ] vcvth_n_f16_u64
 * [ ] vcvth_n_s16_f16
 * [ ] vcvth_n_s32_f16
 * [ ] vcvth_n_s64_f16
 * [x] vcvth_n_u16_f16
 * [ ] vcvth_n_u32_f16
 * [ ] vcvth_n_u64_f16

### cvtm

SIMDe currently implements 11 of 22 (50.00%) functions.

 * [ ] vcvtm_s32_f32
 * [x] vcvtm_u32_f32
 * [ ] vcvtm_s64_f64
 * [x] vcvtm_u64_f64
 * [ ] vcvtm_s16_f16
 * [x] vcvtm_u16_f16
 * [ ] vcvtm_s32_f32
 * [ ] vcvtmq_s32_f32
 * [x] vcvtm_u32_f32
 * [x] vcvtmq_u32_f32
 * [ ] vcvtms_s32_f32
 * [x] vcvtms_u32_f32
 * [ ] vcvtm_s64_f64
 * [ ] vcvtmq_s64_f64
 * [x] vcvtm_u64_f64
 * [x] vcvtmq_u64_f64
 * [ ] vcvtmd_s64_f64
 * [x] vcvtmd_u64_f64
 * [ ] vcvtm_s16_f16
 * [ ] vcvtmq_s16_f16
 * [x] vcvtm_u16_f16
 * [x] vcvtmq_u16_f16

### cvtmh

SIMDe currently implements 10 of 12 (83.33%) functions.

 * [ ] vcvtmh_s16_f16
 * [x] vcvtmh_s32_f16
 * [x] vcvtmh_s64_f16
 * [x] vcvtmh_u16_f16
 * [x] vcvtmh_u32_f16
 * [x] vcvtmh_u64_f16
 * [ ] vcvtmh_s16_f16
 * [x] vcvtmh_s32_f16
 * [x] vcvtmh_s64_f16
 * [x] vcvtmh_u16_f16
 * [x] vcvtmh_u32_f16
 * [x] vcvtmh_u64_f16

### cvtn

SIMDe currently implements 19 of 22 (86.36%) functions.

 * [x] vcvtn_s32_f32
 * [x] vcvtn_u32_f32
 * [x] vcvtn_s64_f64
 * [x] vcvtn_u64_f64
 * [ ] vcvtn_s16_f16
 * [x] vcvtn_u16_f16
 * [x] vcvtn_s32_f32
 * [x] vcvtnq_s32_f32
 * [x] vcvtn_u32_f32
 * [x] vcvtnq_u32_f32
 * [x] vcvtns_s32_f32
 * [x] vcvtns_u32_f32
 * [x] vcvtn_s64_f64
 * [x] vcvtnq_s64_f64
 * [x] vcvtn_u64_f64
 * [x] vcvtnq_u64_f64
 * [x] vcvtnd_s64_f64
 * [x] vcvtnd_u64_f64
 * [ ] vcvtn_s16_f16
 * [ ] vcvtnq_s16_f16
 * [x] vcvtn_u16_f16
 * [x] vcvtnq_u16_f16

### cvtnh

SIMDe currently implements 10 of 12 (83.33%) functions.

 * [ ] vcvtnh_s16_f16
 * [x] vcvtnh_s32_f16
 * [x] vcvtnh_s64_f16
 * [x] vcvtnh_u16_f16
 * [x] vcvtnh_u32_f16
 * [x] vcvtnh_u64_f16
 * [ ] vcvtnh_s16_f16
 * [x] vcvtnh_s32_f16
 * [x] vcvtnh_s64_f16
 * [x] vcvtnh_u16_f16
 * [x] vcvtnh_u32_f16
 * [x] vcvtnh_u64_f16

### cvtp

SIMDe currently implements 11 of 22 (50.00%) functions.

 * [ ] vcvtp_s32_f32
 * [x] vcvtp_u32_f32
 * [ ] vcvtp_s64_f64
 * [x] vcvtp_u64_f64
 * [ ] vcvtp_s16_f16
 * [x] vcvtp_u16_f16
 * [ ] vcvtp_s32_f32
 * [ ] vcvtpq_s32_f32
 * [x] vcvtp_u32_f32
 * [x] vcvtpq_u32_f32
 * [ ] vcvtps_s32_f32
 * [x] vcvtps_u32_f32
 * [ ] vcvtp_s64_f64
 * [ ] vcvtpq_s64_f64
 * [x] vcvtp_u64_f64
 * [x] vcvtpq_u64_f64
 * [ ] vcvtpd_s64_f64
 * [x] vcvtpd_u64_f64
 * [ ] vcvtp_s16_f16
 * [ ] vcvtpq_s16_f16
 * [x] vcvtp_u16_f16
 * [x] vcvtpq_u16_f16

### cvtph

SIMDe currently implements 10 of 12 (83.33%) functions.

 * [ ] vcvtph_s16_f16
 * [x] vcvtph_s32_f16
 * [x] vcvtph_s64_f16
 * [x] vcvtph_u16_f16
 * [x] vcvtph_u32_f16
 * [x] vcvtph_u64_f16
 * [ ] vcvtph_s16_f16
 * [x] vcvtph_s32_f16
 * [x] vcvtph_s64_f16
 * [x] vcvtph_u16_f16
 * [x] vcvtph_u32_f16
 * [x] vcvtph_u64_f16

## Unimplemented Families

There are currently 12 unimplemented families.


## Complete Families

SIMDe contains complete implementations of 378 functions families.

 * aba
 * abal
 * abal_high
 * abd
 * abdh
 * abdl
 * abdl_high
 * abs
 * absh
 * add
 * addh
 * addhn
 * addhn_high
 * addl
 * addl_high
 * addlv
 * addv
 * addw
 * addw_high
 * aes
 * and
 * bcax
 * bfdot
 * bfdot_lane
 * bic
 * bsl
 * cadd_rot
 * cage
 * cageh
 * cagt
 * cagth
 * cale
 * caleh
 * calt
 * calth
 * ceq
 * ceqh
 * ceqz
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
 * cmla
 * cmla_lane
 * cmla_rot
 * cmla_rot_lane
 * cnt
 * combine
 * copy_lane
 * create
 * cvt_high
 * cvt_low
 * cvtx
 * cvtx_high
 * div
 * divh
 * dot
 * dot_lane
 * dup_lane
 * dup_n
 * dupb_lane
 * duph_lane
 * eor
 * eor3
 * ext
 * fma
 * fma_lane
 * fma_n
 * fmah
 * fmah_lane
 * fmlal
 * fmlal_high
 * fmlal_lane
 * fmlal_lane_high
 * fmlal_lane_low
 * fmlal_low
 * fmlsl_high
 * fmlsl_lane_high
 * fmlsl_lane_low
 * fmlsl_low
 * fms
 * fms_lane
 * fms_n
 * fmsh
 * fmsh_lane
 * get_high
 * get_lane
 * get_low
 * hadd
 * hsub
 * ld1
 * ld1_dup
 * ld1_lane
 * ld1_x2
 * ld1_x3
 * ld1_x4
 * ld2
 * ld2_dup
 * ld2_lane
 * ld3
 * ld3_dup
 * ld3_lane
 * ld4
 * ld4_dup
 * ld4_lane
 * ldr
 * max
 * maxh
 * maxnm
 * maxnmh
 * maxnmv
 * maxv
 * min
 * minh
 * minnm
 * minnmh
 * minnmv
 * minv
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
 * mmla
 * mov_n
 * movl
 * movl_high
 * movn
 * movn_high
 * mul
 * mul_lane
 * mul_n
 * mulh
 * mulh_lane
 * mull
 * mull_high
 * mull_high_lane
 * mull_high_n
 * mull_lane
 * mull_n
 * mulx
 * mulx_lane
 * mulx_n
 * mulxh
 * mulxh_lane
 * mvn
 * neg
 * negh
 * orn
 * orr
 * padal
 * padd
 * paddl
 * pmax
 * pmaxnm
 * pmin
 * pminnm
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
 * qmovun_high
 * qmovunh
 * qneg
 * qnegh
 * qrdmlah
 * qrdmlah_lane
 * qrdmlahh
 * qrdmlahh_lane
 * qrdmlsh
 * qrdmlsh_lane
 * qrdmlshh
 * qrdmlshh_lane
 * qrdmulh
 * qrdmulh_lane
 * qrdmulh_n
 * qrdmulhh
 * qrdmulhh_lane
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
 * qshluh_n
 * qshrn_high_n
 * qshrn_n
 * qshrnh_n
 * qshrun_high_n
 * qshrun_n
 * qshrunh_n
 * qsub
 * qsubh
 * qtbl1
 * qtbl2
 * qtbl3
 * qtbl4
 * qtbx1
 * qtbx2
 * qtbx3
 * qtbx4
 * raddhn
 * raddhn_high
 * rax
 * rbit
 * recp
 * recpe
 * recpeh
 * recps
 * recpsh
 * recpxh
 * reinterpret
 * rev16
 * rev32
 * rev64
 * rhadd
 * rnd
 * rnd32x
 * rnd32z
 * rnd64x
 * rnd64z
 * rnda
 * rndah
 * rndh
 * rndi
 * rndih
 * rndm
 * rndmh
 * rndn
 * rndnh
 * rndp
 * rndph
 * rndx
 * rndxh
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
 * set_lane
 * sha1
 * sha1h
 * sha256
 * sha512
 * shl
 * shl_n
 * shll_high_n
 * shll_n
 * shr_n
 * shrn_high_n
 * shrn_n
 * sli_n
 * sm3
 * sm4
 * sqadd
 * sqaddh
 * sqrt
 * sqrth
 * sra_n
 * sri_n
 * st1
 * st1_lane
 * st1_x2
 * st1_x3
 * st1_x4
 * st2
 * st2_lane
 * st3
 * st3_lane
 * st4
 * st4_lane
 * str
 * sub
 * subh
 * subhn
 * subhn_high
 * subl
 * subl_high
 * subw
 * subw_high
 * sudot_lane
 * tbl1
 * tbl2
 * tbl3
 * tbl4
 * tbx1
 * tbx2
 * tbx3
 * tbx4
 * trn
 * trn1
 * trn2
 * tst
 * uqadd
 * uqaddh
 * usdot
 * usdot_lane
 * uzp
 * uzp1
 * uzp2
 * xar
 * zip
 * zip1
 * zip2
