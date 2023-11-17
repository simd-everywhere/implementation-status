# Summary

TL;DR: SIMDe currently implements 6443 out of 6670 (96.60%) NEON functions.  If you don't count bf16 types, it's 6443 / 6466 (99.64%).

SIMDe does not currently support bfloat16 types, so they are excluded from this list (though separate totals are often provided to be transparent about what was skipped.  We do plan to support these types in the future.

# Functions by Architecture

| Architecture | Functions | Functions with supported types | Implemented by SIMDe | Percent implemented |
|--------------|----------:|-------------------------------:|---------------------:|--------------------:|
|        ARMv7 |      3411 |                           3408 |                 3408 |             100.00% |
|        ARMv8 |      4290 |                           4098 |                 4075 |              99.44% |
|      AArch64 |      6670 |                           6466 |                 6443 |              99.64% |

# Families

There are 390 function families in NEON (based on how we define families).  Discounting functions which use unsupported types, SIMDe has completely implemented 385 (98.72%) and partially implemented another 1 (0.26%).

## Incomplete Families

There are currently 1 incomplete families.

### mmla

SIMDe currently implements 5 of 7 (71.43%) functions.

 * [x] vmmlaq_s32
 * [x] vusmmlaq_s32
 * [ ] vbfmmlaq_f32
 * [x] vmmlaq_s32
 * [x] vmmlaq_u32
 * [x] vusmmlaq_s32
 * [ ] vbfmmlaq_f32

## Unimplemented Families

There are currently 1 unimplemented families.

 * bfdot (3 functions)
 * bfdot_lane (6 functions)
 * fmlal (4 functions)
 * fmlal_lane (8 functions)

## Complete Families

SIMDe contains complete implementations of 385 functions families.

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
 * combine (2 functions with unsupported types)
 * copy_lane (6 functions with unsupported types)
 * create (2 functions with unsupported types)
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
 * div
 * divh
 * dot
 * dot_lane
 * dup_lane (6 functions with unsupported types)
 * dup_n (3 functions with unsupported types)
 * dupb_lane
 * duph_lane (4 functions with unsupported types)
 * eor
 * eor3
 * ext
 * fma
 * fma_lane
 * fma_n
 * fmah
 * fmah_lane
 * fmlal_high
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
 * get_high (2 functions with unsupported types)
 * get_lane (3 functions with unsupported types)
 * get_low (2 functions with unsupported types)
 * hadd
 * hsub
 * ld1 (3 functions with unsupported types)
 * ld1_dup (3 functions with unsupported types)
 * ld1_lane (3 functions with unsupported types)
 * ld1_x2 (3 functions with unsupported types)
 * ld1_x3 (3 functions with unsupported types)
 * ld1_x4 (3 functions with unsupported types)
 * ld2 (3 functions with unsupported types)
 * ld2_dup (3 functions with unsupported types)
 * ld2_lane (3 functions with unsupported types)
 * ld3 (3 functions with unsupported types)
 * ld3_dup (3 functions with unsupported types)
 * ld3_lane (3 functions with unsupported types)
 * ld4 (3 functions with unsupported types)
 * ld4_dup (3 functions with unsupported types)
 * ld4_lane (3 functions with unsupported types)
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
 * reinterpret (80 functions with unsupported types)
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
 * set_lane (3 functions with unsupported types)
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
 * st1 (3 functions with unsupported types)
 * st1_lane (3 functions with unsupported types)
 * st1_x2 (3 functions with unsupported types)
 * st1_x3 (3 functions with unsupported types)
 * st1_x4 (3 functions with unsupported types)
 * st2 (3 functions with unsupported types)
 * st2_lane (3 functions with unsupported types)
 * st3 (3 functions with unsupported types)
 * st3_lane (3 functions with unsupported types)
 * st4 (3 functions with unsupported types)
 * st4_lane (3 functions with unsupported types)
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
