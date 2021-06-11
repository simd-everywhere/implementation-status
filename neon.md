# Summary

TL;DR: SIMDe currently implements 3336 out of 6670 (50.01%) NEON functions.  If you don't count 16-bit floats and poly types, it's 3336 / 4969 (67.14%).

SIMDe does not currently support 16-bit floating point types or polynomial types, so they are excluded from this list (though separate totals are often provided to be transparent about what was skipped.  We do plan to support these types in the future.

# Functions by Architecture

| Architecture | Functions | Functions with supported types | Implemented by SIMDe | Percent implemented |
| --: | --: | --: | --: |
|        ARMv7 |      3411 |                           2807 |                 2281 |              81.26% |
|        ARMv8 |      4290 |                           2980 |                 2329 |              78.15% |
|      AArch64 |      6670 |                           4969 |                 3336 |              67.14% |

# Families

There are 390 function families in NEON (based on how we define families).  Discounting functions which use unsupported types, SIMDe has completely implemented 221 (56.67%) and partially implemented another 38 (9.74%).

## Inomplete Families

There are currently 38 incomplete families.

### cvt

SIMDe currently implements 32 of 36 (88.89%) functions, not counting 20 which require currently unsupported types.

 * [x] vcvt_s32_f32
 * [x] vcvt_u32_f32
 * [x] vcvt_s64_f64
 * [x] vcvt_u64_f64
 * [x] vcvt_f32_s32
 * [x] vcvt_f32_u32
 * [x] vcvt_f64_s64
 * [x] vcvt_f64_u64
 * [ ] vcvt_f32_f64
 * [ ] vcvt_f64_f32
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
 * [ ] vcvt_f32_f64
 * [ ] vcvt_f64_f32

### dup_lane

SIMDe currently implements 60 of 72 (83.33%) functions, not counting 30 which require currently unsupported types.

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
 * [ ] vdups_lane_s32
 * [ ] vdupd_lane_s64
 * [ ] vdups_lane_u32
 * [ ] vdupd_lane_u64
 * [ ] vdups_lane_f32
 * [ ] vdupd_lane_f64
 * [ ] vdups_laneq_s32
 * [ ] vdupd_laneq_s64
 * [ ] vdups_laneq_u32
 * [ ] vdupd_laneq_u64
 * [ ] vdups_laneq_f32
 * [ ] vdupd_laneq_f64

### fma_lane

SIMDe currently implements 14 of 16 (87.50%) functions, not counting 6 which require currently unsupported types.

 * [x] vfma_lane_f32
 * [x] vfma_lane_f64
 * [x] vfma_laneq_f32
 * [x] vfma_laneq_f64
 * [x] vfma_lane_f32
 * [ ] vfmaq_lane_f32
 * [x] vfma_lane_f64
 * [ ] vfmaq_lane_f64
 * [x] vfmas_lane_f32
 * [x] vfmad_lane_f64
 * [x] vfma_laneq_f32
 * [x] vfmaq_laneq_f32
 * [x] vfma_laneq_f64
 * [x] vfmaq_laneq_f64
 * [x] vfmas_laneq_f32
 * [x] vfmad_laneq_f64

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

### ld1_lane

SIMDe currently implements 18 of 30 (60.00%) functions, not counting 15 which require currently unsupported types.

 * [x] vld1_lane_s8
 * [x] vld1_lane_s16
 * [x] vld1_lane_s32
 * [ ] vld1_lane_s64
 * [x] vld1_lane_u8
 * [x] vld1_lane_u16
 * [x] vld1_lane_u32
 * [ ] vld1_lane_u64
 * [ ] vld1_lane_f32
 * [ ] vld1_lane_f64
 * [x] vld1_lane_s8
 * [x] vld1q_lane_s8
 * [x] vld1_lane_s16
 * [x] vld1q_lane_s16
 * [x] vld1_lane_s32
 * [x] vld1q_lane_s32
 * [ ] vld1_lane_s64
 * [ ] vld1q_lane_s64
 * [x] vld1_lane_u8
 * [x] vld1q_lane_u8
 * [x] vld1_lane_u16
 * [x] vld1q_lane_u16
 * [x] vld1_lane_u32
 * [x] vld1q_lane_u32
 * [ ] vld1_lane_u64
 * [ ] vld1q_lane_u64
 * [ ] vld1_lane_f32
 * [ ] vld1q_lane_f32
 * [ ] vld1_lane_f64
 * [ ] vld1q_lane_f64

### ld2

SIMDe currently implements 10 of 30 (33.33%) functions, not counting 15 which require currently unsupported types.

 * [ ] vld2_s8
 * [ ] vld2_s16
 * [ ] vld2_s32
 * [x] vld2_u8
 * [x] vld2_u16
 * [x] vld2_u32
 * [ ] vld2_f32
 * [ ] vld2_s64
 * [ ] vld2_u64
 * [ ] vld2_f64
 * [ ] vld2_s8
 * [ ] vld2q_s8
 * [ ] vld2_s16
 * [ ] vld2q_s16
 * [ ] vld2_s32
 * [ ] vld2q_s32
 * [x] vld2_u8
 * [x] vld2q_u8
 * [x] vld2_u16
 * [x] vld2q_u16
 * [x] vld2_u32
 * [x] vld2q_u32
 * [ ] vld2_f32
 * [x] vld2q_f32
 * [ ] vld2_s64
 * [ ] vld2_u64
 * [ ] vld2q_s64
 * [ ] vld2q_u64
 * [ ] vld2_f64
 * [ ] vld2q_f64

### ld4_lane

SIMDe currently implements 12 of 30 (40.00%) functions, not counting 15 which require currently unsupported types.

 * [x] vld4_lane_s16
 * [x] vld4_lane_s32
 * [x] vld4_lane_u16
 * [x] vld4_lane_u32
 * [ ] vld4_lane_f32
 * [x] vld4_lane_s8
 * [x] vld4_lane_u8
 * [ ] vld4_lane_s64
 * [ ] vld4_lane_u64
 * [ ] vld4_lane_f64
 * [x] vld4_lane_s16
 * [ ] vld4q_lane_s16
 * [x] vld4_lane_s32
 * [ ] vld4q_lane_s32
 * [x] vld4_lane_u16
 * [ ] vld4q_lane_u16
 * [x] vld4_lane_u32
 * [ ] vld4q_lane_u32
 * [ ] vld4_lane_f32
 * [ ] vld4q_lane_f32
 * [x] vld4_lane_s8
 * [x] vld4_lane_u8
 * [ ] vld4q_lane_s8
 * [ ] vld4q_lane_u8
 * [ ] vld4_lane_s64
 * [ ] vld4q_lane_s64
 * [ ] vld4_lane_u64
 * [ ] vld4q_lane_u64
 * [ ] vld4_lane_f64
 * [ ] vld4q_lane_f64

### mul_lane

SIMDe currently implements 32 of 40 (80.00%) functions, not counting 6 which require currently unsupported types.

 * [x] vmul_lane_s16
 * [x] vmul_lane_s32
 * [x] vmul_lane_u16
 * [x] vmul_lane_u32
 * [x] vmul_lane_f32
 * [x] vmul_lane_f64
 * [ ] vmul_laneq_s16
 * [ ] vmul_laneq_s32
 * [ ] vmul_laneq_u16
 * [ ] vmul_laneq_u32
 * [x] vmul_laneq_f32
 * [x] vmul_laneq_f64
 * [x] vmul_lane_s16
 * [x] vmulq_lane_s16
 * [x] vmul_lane_s32
 * [x] vmulq_lane_s32
 * [x] vmul_lane_u16
 * [x] vmulq_lane_u16
 * [x] vmul_lane_u32
 * [x] vmulq_lane_u32
 * [x] vmul_lane_f32
 * [x] vmulq_lane_f32
 * [x] vmul_lane_f64
 * [x] vmulq_lane_f64
 * [x] vmuls_lane_f32
 * [x] vmuld_lane_f64
 * [ ] vmul_laneq_s16
 * [x] vmulq_laneq_s16
 * [ ] vmul_laneq_s32
 * [x] vmulq_laneq_s32
 * [ ] vmul_laneq_u16
 * [x] vmulq_laneq_u16
 * [ ] vmul_laneq_u32
 * [x] vmulq_laneq_u32
 * [x] vmul_laneq_f32
 * [x] vmulq_laneq_f32
 * [x] vmul_laneq_f64
 * [x] vmulq_laneq_f64
 * [x] vmuls_laneq_f32
 * [x] vmuld_laneq_f64

### neg

SIMDe currently implements 18 of 19 (94.74%) functions, not counting 3 which require currently unsupported types.

 * [x] vneg_s8
 * [x] vneg_s16
 * [x] vneg_s32
 * [x] vneg_f32
 * [x] vneg_s64
 * [x] vneg_f64
 * [x] vneg_s8
 * [x] vnegq_s8
 * [x] vneg_s16
 * [x] vnegq_s16
 * [x] vneg_s32
 * [x] vnegq_s32
 * [x] vneg_f32
 * [x] vnegq_f32
 * [x] vneg_s64
 * [ ] vnegd_s64
 * [x] vnegq_s64
 * [x] vneg_f64
 * [x] vnegq_f64

### padd

SIMDe currently implements 24 of 28 (85.71%) functions, not counting 3 which require currently unsupported types.

 * [x] vpadd_s8
 * [x] vpadd_s16
 * [x] vpadd_s32
 * [x] vpadd_u8
 * [x] vpadd_u16
 * [x] vpadd_u32
 * [x] vpadd_f32
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
 * [ ] vpaddd_s64
 * [ ] vpaddd_u64
 * [ ] vpadds_f32
 * [ ] vpaddd_f64

### pmax

SIMDe currently implements 22 of 25 (88.00%) functions, not counting 3 which require currently unsupported types.

 * [x] vpmax_s8
 * [x] vpmax_s16
 * [x] vpmax_s32
 * [x] vpmax_u8
 * [x] vpmax_u16
 * [x] vpmax_u32
 * [x] vpmax_f32
 * [ ] vpmaxqd_f64
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
 * [ ] vpmaxs_f32
 * [ ] vpmaxqd_f64

### pmin

SIMDe currently implements 22 of 25 (88.00%) functions, not counting 3 which require currently unsupported types.

 * [x] vpmin_s8
 * [x] vpmin_s16
 * [x] vpmin_s32
 * [x] vpmin_u8
 * [x] vpmin_u16
 * [x] vpmin_u32
 * [x] vpmin_f32
 * [ ] vpminqd_f64
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
 * [ ] vpmins_f32
 * [ ] vpminqd_f64

### qdmulh

SIMDe currently implements 6 of 7 (85.71%) functions.

 * [x] vqdmulh_s16
 * [x] vqdmulh_s32
 * [x] vqdmulh_s16
 * [x] vqdmulhq_s16
 * [x] vqdmulh_s32
 * [x] vqdmulhq_s32
 * [ ] vqdmulhs_s32

### qdmulh_lane

SIMDe currently implements 6 of 14 (42.86%) functions.

 * [x] vqdmulh_lane_s16
 * [x] vqdmulh_lane_s32
 * [ ] vqdmulh_laneq_s16
 * [ ] vqdmulh_laneq_s32
 * [x] vqdmulh_lane_s16
 * [x] vqdmulhq_lane_s16
 * [x] vqdmulh_lane_s32
 * [x] vqdmulhq_lane_s32
 * [ ] vqdmulhs_lane_s32
 * [ ] vqdmulh_laneq_s16
 * [ ] vqdmulhq_laneq_s16
 * [ ] vqdmulh_laneq_s32
 * [ ] vqdmulhq_laneq_s32
 * [ ] vqdmulhs_laneq_s32

### qrdmulh_lane

SIMDe currently implements 12 of 14 (85.71%) functions.

 * [x] vqrdmulh_lane_s16
 * [x] vqrdmulh_lane_s32
 * [x] vqrdmulh_laneq_s16
 * [x] vqrdmulh_laneq_s32
 * [x] vqrdmulh_lane_s16
 * [x] vqrdmulhq_lane_s16
 * [x] vqrdmulh_lane_s32
 * [x] vqrdmulhq_lane_s32
 * [ ] vqrdmulhs_lane_s32
 * [x] vqrdmulh_laneq_s16
 * [x] vqrdmulhq_laneq_s16
 * [x] vqrdmulh_laneq_s32
 * [x] vqrdmulhq_laneq_s32
 * [ ] vqrdmulhs_laneq_s32

### qrshrn_n

SIMDe currently implements 12 of 16 (75.00%) functions.

 * [x] vqrshrn_n_s16
 * [x] vqrshrn_n_s32
 * [x] vqrshrn_n_s64
 * [x] vqrshrn_n_u16
 * [x] vqrshrn_n_u32
 * [x] vqrshrn_n_u64
 * [x] vqrshrn_n_s16
 * [x] vqrshrn_n_s32
 * [x] vqrshrn_n_s64
 * [x] vqrshrn_n_u16
 * [x] vqrshrn_n_u32
 * [x] vqrshrn_n_u64
 * [ ] vqrshrns_n_s32
 * [ ] vqrshrnd_n_s64
 * [ ] vqrshrns_n_u32
 * [ ] vqrshrnd_n_u64

### qrshrun_n

SIMDe currently implements 6 of 8 (75.00%) functions.

 * [x] vqrshrun_n_s16
 * [x] vqrshrun_n_s32
 * [x] vqrshrun_n_s64
 * [x] vqrshrun_n_s16
 * [x] vqrshrun_n_s32
 * [x] vqrshrun_n_s64
 * [ ] vqrshruns_n_s32
 * [ ] vqrshrund_n_s64

### qshlu_n

SIMDe currently implements 12 of 15 (80.00%) functions.

 * [x] vqshlu_n_s8
 * [x] vqshlu_n_s16
 * [x] vqshlu_n_s32
 * [x] vqshlu_n_s64
 * [x] vqshlu_n_s8
 * [x] vqshluq_n_s8
 * [x] vqshlu_n_s16
 * [x] vqshluq_n_s16
 * [x] vqshlu_n_s32
 * [x] vqshluq_n_s32
 * [x] vqshlu_n_s64
 * [x] vqshluq_n_s64
 * [ ] vqshlub_n_s8
 * [ ] vqshlus_n_s32
 * [ ] vqshlud_n_s64

### qshrn_n

SIMDe currently implements 12 of 16 (75.00%) functions.

 * [x] vqshrn_n_s16
 * [x] vqshrn_n_s32
 * [x] vqshrn_n_s64
 * [x] vqshrn_n_u16
 * [x] vqshrn_n_u32
 * [x] vqshrn_n_u64
 * [x] vqshrn_n_s16
 * [x] vqshrn_n_s32
 * [x] vqshrn_n_s64
 * [x] vqshrn_n_u16
 * [x] vqshrn_n_u32
 * [x] vqshrn_n_u64
 * [ ] vqshrns_n_s32
 * [ ] vqshrnd_n_s64
 * [ ] vqshrns_n_u32
 * [ ] vqshrnd_n_u64

### qshrun_n

SIMDe currently implements 6 of 8 (75.00%) functions.

 * [x] vqshrun_n_s16
 * [x] vqshrun_n_s32
 * [x] vqshrun_n_s64
 * [x] vqshrun_n_s16
 * [x] vqshrun_n_s32
 * [x] vqshrun_n_s64
 * [ ] vqshruns_n_s32
 * [ ] vqshrund_n_s64

### recpe

SIMDe currently implements 3 of 11 (27.27%) functions, not counting 3 which require currently unsupported types.

 * [ ] vrecpe_u32
 * [x] vrecpe_f32
 * [ ] vrecpe_f64
 * [ ] vrecpe_u32
 * [ ] vrecpeq_u32
 * [x] vrecpe_f32
 * [x] vrecpeq_f32
 * [ ] vrecpe_f64
 * [ ] vrecpeq_f64
 * [ ] vrecpes_f32
 * [ ] vrecped_f64

### recps

SIMDe currently implements 2 of 7 (28.57%) functions, not counting 3 which require currently unsupported types.

 * [ ] vrecps_f64
 * [x] vrecps_f32
 * [x] vrecpsq_f32
 * [ ] vrecps_f64
 * [ ] vrecpsq_f64
 * [ ] vrecpss_f32
 * [ ] vrecpsd_f64

### rndn

SIMDe currently implements 6 of 7 (85.71%) functions, not counting 3 which require currently unsupported types.

 * [x] vrndn_f32
 * [x] vrndn_f64
 * [x] vrndn_f32
 * [x] vrndnq_f32
 * [x] vrndn_f64
 * [x] vrndnq_f64
 * [ ] vrndns_f32

### rshl

SIMDe currently implements 24 of 26 (92.31%) functions.

 * [x] vrshl_s8
 * [x] vrshl_s16
 * [x] vrshl_s32
 * [x] vrshl_s64
 * [x] vrshl_u8
 * [x] vrshl_u16
 * [x] vrshl_u32
 * [x] vrshl_u64
 * [x] vrshl_s8
 * [x] vrshlq_s8
 * [x] vrshl_s16
 * [x] vrshlq_s16
 * [x] vrshl_s32
 * [x] vrshlq_s32
 * [x] vrshl_s64
 * [x] vrshlq_s64
 * [x] vrshl_u8
 * [x] vrshlq_u8
 * [x] vrshl_u16
 * [x] vrshlq_u16
 * [x] vrshl_u32
 * [x] vrshlq_u32
 * [x] vrshl_u64
 * [x] vrshlq_u64
 * [ ] vrshld_s64
 * [ ] vrshld_u64

### rshr_n

SIMDe currently implements 24 of 26 (92.31%) functions.

 * [x] vrshr_n_s8
 * [x] vrshr_n_s16
 * [x] vrshr_n_s32
 * [x] vrshr_n_s64
 * [x] vrshr_n_u8
 * [x] vrshr_n_u16
 * [x] vrshr_n_u32
 * [x] vrshr_n_u64
 * [x] vrshr_n_s8
 * [x] vrshrq_n_s8
 * [x] vrshr_n_s16
 * [x] vrshrq_n_s16
 * [x] vrshr_n_s32
 * [x] vrshrq_n_s32
 * [x] vrshr_n_s64
 * [x] vrshrq_n_s64
 * [x] vrshr_n_u8
 * [x] vrshrq_n_u8
 * [x] vrshr_n_u16
 * [x] vrshrq_n_u16
 * [x] vrshr_n_u32
 * [x] vrshrq_n_u32
 * [x] vrshr_n_u64
 * [x] vrshrq_n_u64
 * [ ] vrshrd_n_s64
 * [ ] vrshrd_n_u64

### rsqrte

SIMDe currently implements 3 of 11 (27.27%) functions, not counting 3 which require currently unsupported types.

 * [ ] vrsqrte_u32
 * [x] vrsqrte_f32
 * [ ] vrsqrte_f64
 * [ ] vrsqrte_u32
 * [ ] vrsqrteq_u32
 * [x] vrsqrte_f32
 * [x] vrsqrteq_f32
 * [ ] vrsqrte_f64
 * [ ] vrsqrteq_f64
 * [ ] vrsqrtes_f32
 * [ ] vrsqrted_f64

### rsqrts

SIMDe currently implements 2 of 7 (28.57%) functions, not counting 3 which require currently unsupported types.

 * [ ] vrsqrts_f64
 * [x] vrsqrts_f32
 * [x] vrsqrtsq_f32
 * [ ] vrsqrts_f64
 * [ ] vrsqrtsq_f64
 * [ ] vrsqrtss_f32
 * [ ] vrsqrtsd_f64

### rsra_n

SIMDe currently implements 24 of 26 (92.31%) functions.

 * [x] vrsra_n_s8
 * [x] vrsra_n_s16
 * [x] vrsra_n_s32
 * [x] vrsra_n_s64
 * [x] vrsra_n_u8
 * [x] vrsra_n_u16
 * [x] vrsra_n_u32
 * [x] vrsra_n_u64
 * [x] vrsra_n_s8
 * [x] vrsraq_n_s8
 * [x] vrsra_n_s16
 * [x] vrsraq_n_s16
 * [x] vrsra_n_s32
 * [x] vrsraq_n_s32
 * [x] vrsra_n_s64
 * [x] vrsraq_n_s64
 * [x] vrsra_n_u8
 * [x] vrsraq_n_u8
 * [x] vrsra_n_u16
 * [x] vrsraq_n_u16
 * [x] vrsra_n_u32
 * [x] vrsraq_n_u32
 * [x] vrsra_n_u64
 * [x] vrsraq_n_u64
 * [ ] vrsrad_n_s64
 * [ ] vrsrad_n_u64

### shl

SIMDe currently implements 24 of 26 (92.31%) functions.

 * [x] vshl_s8
 * [x] vshl_s16
 * [x] vshl_s32
 * [x] vshl_s64
 * [x] vshl_u8
 * [x] vshl_u16
 * [x] vshl_u32
 * [x] vshl_u64
 * [x] vshl_s8
 * [x] vshlq_s8
 * [x] vshl_s16
 * [x] vshlq_s16
 * [x] vshl_s32
 * [x] vshlq_s32
 * [x] vshl_s64
 * [x] vshlq_s64
 * [x] vshl_u8
 * [x] vshlq_u8
 * [x] vshl_u16
 * [x] vshlq_u16
 * [x] vshl_u32
 * [x] vshlq_u32
 * [x] vshl_u64
 * [x] vshlq_u64
 * [ ] vshld_s64
 * [ ] vshld_u64

### shl_n

SIMDe currently implements 24 of 26 (92.31%) functions.

 * [x] vshl_n_s8
 * [x] vshl_n_s16
 * [x] vshl_n_s32
 * [x] vshl_n_s64
 * [x] vshl_n_u8
 * [x] vshl_n_u16
 * [x] vshl_n_u32
 * [x] vshl_n_u64
 * [x] vshl_n_s8
 * [x] vshlq_n_s8
 * [x] vshl_n_s16
 * [x] vshlq_n_s16
 * [x] vshl_n_s32
 * [x] vshlq_n_s32
 * [x] vshl_n_s64
 * [x] vshlq_n_s64
 * [x] vshl_n_u8
 * [x] vshlq_n_u8
 * [x] vshl_n_u16
 * [x] vshlq_n_u16
 * [x] vshl_n_u32
 * [x] vshlq_n_u32
 * [x] vshl_n_u64
 * [x] vshlq_n_u64
 * [ ] vshld_n_s64
 * [ ] vshld_n_u64

### shr_n

SIMDe currently implements 24 of 26 (92.31%) functions.

 * [x] vshr_n_s8
 * [x] vshr_n_s16
 * [x] vshr_n_s32
 * [x] vshr_n_s64
 * [x] vshr_n_u8
 * [x] vshr_n_u16
 * [x] vshr_n_u32
 * [x] vshr_n_u64
 * [x] vshr_n_s8
 * [x] vshrq_n_s8
 * [x] vshr_n_s16
 * [x] vshrq_n_s16
 * [x] vshr_n_s32
 * [x] vshrq_n_s32
 * [x] vshr_n_s64
 * [x] vshrq_n_s64
 * [x] vshr_n_u8
 * [x] vshrq_n_u8
 * [x] vshr_n_u16
 * [x] vshrq_n_u16
 * [x] vshr_n_u32
 * [x] vshrq_n_u32
 * [x] vshr_n_u64
 * [x] vshrq_n_u64
 * [ ] vshrd_n_s64
 * [ ] vshrd_n_u64

### sra_n

SIMDe currently implements 24 of 26 (92.31%) functions.

 * [x] vsra_n_s8
 * [x] vsra_n_s16
 * [x] vsra_n_s32
 * [x] vsra_n_s64
 * [x] vsra_n_u8
 * [x] vsra_n_u16
 * [x] vsra_n_u32
 * [x] vsra_n_u64
 * [x] vsra_n_s8
 * [x] vsraq_n_s8
 * [x] vsra_n_s16
 * [x] vsraq_n_s16
 * [x] vsra_n_s32
 * [x] vsraq_n_s32
 * [x] vsra_n_s64
 * [x] vsraq_n_s64
 * [x] vsra_n_u8
 * [x] vsraq_n_u8
 * [x] vsra_n_u16
 * [x] vsraq_n_u16
 * [x] vsra_n_u32
 * [x] vsraq_n_u32
 * [x] vsra_n_u64
 * [x] vsraq_n_u64
 * [ ] vsrad_n_s64
 * [ ] vsrad_n_u64

### sri_n

SIMDe currently implements 24 of 26 (92.31%) functions, not counting 9 which require currently unsupported types.

 * [x] vsri_n_s8
 * [x] vsri_n_s16
 * [x] vsri_n_s32
 * [x] vsri_n_s64
 * [x] vsri_n_u8
 * [x] vsri_n_u16
 * [x] vsri_n_u32
 * [x] vsri_n_u64
 * [x] vsri_n_s8
 * [x] vsriq_n_s8
 * [x] vsri_n_s16
 * [x] vsriq_n_s16
 * [x] vsri_n_s32
 * [x] vsriq_n_s32
 * [x] vsri_n_s64
 * [x] vsriq_n_s64
 * [x] vsri_n_u8
 * [x] vsriq_n_u8
 * [x] vsri_n_u16
 * [x] vsriq_n_u16
 * [x] vsri_n_u32
 * [x] vsriq_n_u32
 * [x] vsri_n_u64
 * [x] vsriq_n_u64
 * [ ] vsrid_n_s64
 * [ ] vsrid_n_u64

### st2

SIMDe currently implements 21 of 30 (70.00%) functions, not counting 15 which require currently unsupported types.

 * [x] vst2_s8
 * [x] vst2_s16
 * [x] vst2_s32
 * [x] vst2_u8
 * [x] vst2_u16
 * [x] vst2_u32
 * [x] vst2_f32
 * [ ] vst2_s64
 * [ ] vst2_u64
 * [ ] vst2_f64
 * [x] vst2_s8
 * [x] vst2q_s8
 * [x] vst2_s16
 * [x] vst2q_s16
 * [x] vst2_s32
 * [x] vst2q_s32
 * [x] vst2_u8
 * [x] vst2q_u8
 * [x] vst2_u16
 * [x] vst2q_u16
 * [x] vst2_u32
 * [x] vst2q_u32
 * [x] vst2_f32
 * [x] vst2q_f32
 * [ ] vst2_s64
 * [ ] vst2_u64
 * [ ] vst2q_s64
 * [ ] vst2q_u64
 * [ ] vst2_f64
 * [ ] vst2q_f64

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

### sub

SIMDe currently implements 28 of 30 (93.33%) functions, not counting 3 which require currently unsupported types.

 * [x] vsub_s16
 * [x] vsub_s32
 * [x] vsub_s64
 * [x] vsub_u16
 * [x] vsub_u32
 * [x] vsub_u64
 * [x] vsub_f32
 * [x] vsub_f64
 * [x] vsub_s8
 * [x] vsubq_s8
 * [x] vsub_s16
 * [x] vsubq_s16
 * [x] vsub_s32
 * [x] vsubq_s32
 * [x] vsub_s64
 * [x] vsubq_s64
 * [x] vsub_u8
 * [x] vsubq_u8
 * [x] vsub_u16
 * [x] vsubq_u16
 * [x] vsub_u32
 * [x] vsubq_u32
 * [x] vsub_u64
 * [x] vsubq_u64
 * [x] vsub_f32
 * [x] vsubq_f32
 * [x] vsub_f64
 * [x] vsubq_f64
 * [ ] vsubd_s64
 * [ ] vsubd_u64

## Unimplemented Families

There are currently 38 unimplemented families.

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

SIMDe contains complete implementations of 221 functions families.

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
 * dup_n (15 functions with unsupported types)
 * eor
 * ext (12 functions with unsupported types)
 * fma (3 functions with unsupported types)
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
 * ld3 (15 functions with unsupported types)
 * ld4 (15 functions with unsupported types)
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
 * negh (2 functions with unsupported types)
 * orn
 * orr
 * padal
 * paddl
 * qabs
 * qabsh
 * qadd
 * qaddh
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
 * qrdmulh_n
 * qrdmulhh
 * qshl
 * qshlh
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
 * recpeh (2 functions with unsupported types)
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
 * rndnh (2 functions with unsupported types)
 * rndp (3 functions with unsupported types)
 * rndph (2 functions with unsupported types)
 * rndxh (2 functions with unsupported types)
 * rshrn_n
 * rsqrteh (2 functions with unsupported types)
 * rsqrtsh (2 functions with unsupported types)
 * set_lane (15 functions with unsupported types)
 * shll_n
 * shrn_n
 * sqadd
 * sqaddh
 * sqrth (2 functions with unsupported types)
 * st1 (15 functions with unsupported types)
 * st1_lane (15 functions with unsupported types)
 * st3 (15 functions with unsupported types)
 * st4 (15 functions with unsupported types)
 * str (2 functions with unsupported types)
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
