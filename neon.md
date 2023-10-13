# Summary

TL;DR: SIMDe currently implements 3921 out of 6670 (58.79%) NEON functions.  If you don't count poly types, it's 3921 / 5692 (68.89%).

SIMDe does not currently support polynomial types, so they are excluded from this list (though separate totals are often provided to be transparent about what was skipped.  We do plan to support these types in the future.

# Functions by Architecture

| Architecture | Functions | Functions with supported types | Implemented by SIMDe | Percent implemented |
|--------------|----------:|-------------------------------:|---------------------:|--------------------:|
|        ARMv7 |      3411 |                           2984 |                 2511 |              84.15% |
|        ARMv8 |      4290 |                           3479 |                 2658 |              76.40% |
|      AArch64 |      6670 |                           5692 |                 3921 |              68.89% |

# Families

There are 390 function families in NEON (based on how we define families).  Discounting functions which use unsupported types, SIMDe has completely implemented 178 (45.64%) and partially implemented another 53 (13.59%).

## Incomplete Families

There are currently 53 incomplete families.

### abd

SIMDe currently implements 25 of 28 (89.29%) functions.

 * [x] vabd_s8
 * [x] vabd_s16
 * [x] vabd_s32
 * [x] vabd_u8
 * [x] vabd_u16
 * [x] vabd_u32
 * [x] vabd_f32
 * [ ] vabd_f16
 * [x] vabd_s8
 * [x] vabdq_s8
 * [x] vabd_s16
 * [x] vabdq_s16
 * [x] vabd_s32
 * [x] vabdq_s32
 * [x] vabd_u8
 * [x] vabdq_u8
 * [x] vabd_u16
 * [x] vabdq_u16
 * [x] vabd_u32
 * [x] vabdq_u32
 * [x] vabd_f32
 * [x] vabdq_f32
 * [x] vabd_f64
 * [x] vabdq_f64
 * [x] vabds_f32
 * [x] vabdd_f64
 * [ ] vabd_f16
 * [ ] vabdq_f16

### cgez

SIMDe currently implements 21 of 24 (87.50%) functions.

 * [x] vcgez_s8
 * [x] vcgez_s16
 * [x] vcgez_s32
 * [x] vcgez_s64
 * [x] vcgez_f32
 * [x] vcgez_f64
 * [ ] vcgez_f16
 * [x] vcgez_s8
 * [x] vcgezq_s8
 * [x] vcgez_s16
 * [x] vcgezq_s16
 * [x] vcgez_s32
 * [x] vcgezq_s32
 * [x] vcgez_s64
 * [x] vcgezq_s64
 * [x] vcgez_f32
 * [x] vcgezq_f32
 * [x] vcgez_f64
 * [x] vcgezq_f64
 * [x] vcgezd_s64
 * [x] vcgezs_f32
 * [x] vcgezd_f64
 * [ ] vcgez_f16
 * [ ] vcgezq_f16

### cgtz

SIMDe currently implements 21 of 24 (87.50%) functions.

 * [x] vcgtz_s8
 * [x] vcgtz_s16
 * [x] vcgtz_s32
 * [x] vcgtz_s64
 * [x] vcgtz_f32
 * [x] vcgtz_f64
 * [ ] vcgtz_f16
 * [x] vcgtz_s8
 * [x] vcgtzq_s8
 * [x] vcgtz_s16
 * [x] vcgtzq_s16
 * [x] vcgtz_s32
 * [x] vcgtzq_s32
 * [x] vcgtz_s64
 * [x] vcgtzq_s64
 * [x] vcgtz_f32
 * [x] vcgtzq_f32
 * [x] vcgtz_f64
 * [x] vcgtzq_f64
 * [x] vcgtzd_s64
 * [x] vcgtzs_f32
 * [x] vcgtzd_f64
 * [ ] vcgtz_f16
 * [ ] vcgtzq_f16

### cle

SIMDe currently implements 34 of 37 (91.89%) functions.

 * [x] vcle_s8
 * [x] vcle_s16
 * [x] vcle_s32
 * [x] vcle_u8
 * [x] vcle_u16
 * [x] vcle_u32
 * [x] vcle_f32
 * [x] vcle_s64
 * [x] vcle_u64
 * [x] vcle_f64
 * [ ] vcle_f16
 * [x] vcle_s8
 * [x] vcleq_s8
 * [x] vcle_s16
 * [x] vcleq_s16
 * [x] vcle_s32
 * [x] vcleq_s32
 * [x] vcle_u8
 * [x] vcleq_u8
 * [x] vcle_u16
 * [x] vcleq_u16
 * [x] vcle_u32
 * [x] vcleq_u32
 * [x] vcle_f32
 * [x] vcleq_f32
 * [x] vcle_s64
 * [x] vcleq_s64
 * [x] vcle_u64
 * [x] vcleq_u64
 * [x] vcle_f64
 * [x] vcleq_f64
 * [x] vcled_s64
 * [x] vcled_u64
 * [x] vcles_f32
 * [x] vcled_f64
 * [ ] vcle_f16
 * [ ] vcleq_f16

### cltz

SIMDe currently implements 21 of 24 (87.50%) functions.

 * [x] vcltz_s8
 * [x] vcltz_s16
 * [x] vcltz_s32
 * [x] vcltz_s64
 * [x] vcltz_f32
 * [x] vcltz_f64
 * [ ] vcltz_f16
 * [x] vcltz_s8
 * [x] vcltzq_s8
 * [x] vcltz_s16
 * [x] vcltzq_s16
 * [x] vcltz_s32
 * [x] vcltzq_s32
 * [x] vcltz_s64
 * [x] vcltzq_s64
 * [x] vcltz_f32
 * [x] vcltzq_f32
 * [x] vcltz_f64
 * [x] vcltzq_f64
 * [x] vcltzd_s64
 * [x] vcltzs_f32
 * [x] vcltzd_f64
 * [ ] vcltz_f16
 * [ ] vcltzq_f16

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

### create

SIMDe currently implements 20 of 22 (90.91%) functions, not counting 8 which require currently unsupported types.

 * [x] vcreate_s8
 * [x] vcreate_s16
 * [x] vcreate_s32
 * [x] vcreate_s64
 * [x] vcreate_u8
 * [x] vcreate_u16
 * [x] vcreate_u32
 * [x] vcreate_u64
 * [ ] vcreate_f16
 * [x] vcreate_f32
 * [x] vcreate_f64
 * [x] vcreate_s8
 * [x] vcreate_s16
 * [x] vcreate_s32
 * [x] vcreate_s64
 * [x] vcreate_u8
 * [x] vcreate_u16
 * [x] vcreate_u32
 * [x] vcreate_u64
 * [ ] vcreate_f16
 * [x] vcreate_f32
 * [x] vcreate_f64

### cvta

SIMDe currently implements 8 of 22 (36.36%) functions.

 * [x] vcvta_s32_f32
 * [x] vcvta_u32_f32
 * [ ] vcvta_s64_f64
 * [ ] vcvta_u64_f64
 * [ ] vcvta_s16_f16
 * [ ] vcvta_u16_f16
 * [x] vcvta_s32_f32
 * [x] vcvtaq_s32_f32
 * [x] vcvta_u32_f32
 * [x] vcvtaq_u32_f32
 * [x] vcvtas_s32_f32
 * [x] vcvtas_u32_f32
 * [ ] vcvta_s64_f64
 * [ ] vcvtaq_s64_f64
 * [ ] vcvta_u64_f64
 * [ ] vcvtaq_u64_f64
 * [ ] vcvtad_s64_f64
 * [ ] vcvtad_u64_f64
 * [ ] vcvta_s16_f16
 * [ ] vcvtaq_s16_f16
 * [ ] vcvta_u16_f16
 * [ ] vcvtaq_u16_f16

### cvtn

SIMDe currently implements 6 of 22 (27.27%) functions.

 * [ ] vcvtn_s32_f32
 * [ ] vcvtn_u32_f32
 * [ ] vcvtn_s64_f64
 * [ ] vcvtn_u64_f64
 * [ ] vcvtn_s16_f16
 * [ ] vcvtn_u16_f16
 * [ ] vcvtn_s32_f32
 * [x] vcvtnq_s32_f32
 * [ ] vcvtn_u32_f32
 * [x] vcvtnq_u32_f32
 * [ ] vcvtns_s32_f32
 * [x] vcvtns_u32_f32
 * [ ] vcvtn_s64_f64
 * [x] vcvtnq_s64_f64
 * [ ] vcvtn_u64_f64
 * [x] vcvtnq_u64_f64
 * [ ] vcvtnd_s64_f64
 * [x] vcvtnd_u64_f64
 * [ ] vcvtn_s16_f16
 * [ ] vcvtnq_s16_f16
 * [ ] vcvtn_u16_f16
 * [ ] vcvtnq_u16_f16

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

SIMDe currently implements 72 of 78 (92.31%) functions, not counting 24 which require currently unsupported types.

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
 * [ ] vdup_lane_f16
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
 * [ ] vdup_lane_f16
 * [ ] vdupq_lane_f16
 * [ ] vdup_laneq_f16
 * [ ] vdupq_laneq_f16

### ext

SIMDe currently implements 31 of 33 (93.94%) functions, not counting 9 which require currently unsupported types.

 * [x] vext_s8
 * [x] vext_s16
 * [x] vext_s32
 * [x] vext_s64
 * [x] vext_u8
 * [x] vext_u16
 * [x] vext_u32
 * [x] vext_u64
 * [x] vext_f32
 * [x] vext_f64
 * [ ] vext_f16
 * [x] vext_s8
 * [x] vextq_s8
 * [x] vext_s16
 * [x] vextq_s16
 * [x] vext_s32
 * [x] vextq_s32
 * [x] vext_s64
 * [x] vextq_s64
 * [x] vext_u8
 * [x] vextq_u8
 * [x] vext_u16
 * [x] vextq_u16
 * [x] vext_u32
 * [x] vextq_u32
 * [x] vext_u64
 * [x] vextq_u64
 * [x] vext_f32
 * [x] vextq_f32
 * [x] vext_f64
 * [x] vextq_f64
 * [ ] vext_f16
 * [x] vextq_f16

### fma

SIMDe currently implements 7 of 9 (77.78%) functions.

 * [x] vfma_f32
 * [x] vfma_f64
 * [ ] vfma_f16
 * [x] vfma_f32
 * [x] vfmaq_f32
 * [x] vfma_f64
 * [x] vfmaq_f64
 * [ ] vfma_f16
 * [x] vfmaq_f16

### fma_lane

SIMDe currently implements 16 of 22 (72.73%) functions.

 * [x] vfma_lane_f32
 * [x] vfma_lane_f64
 * [x] vfma_laneq_f32
 * [x] vfma_laneq_f64
 * [ ] vfma_lane_f16
 * [ ] vfma_laneq_f16
 * [x] vfma_lane_f32
 * [x] vfmaq_lane_f32
 * [x] vfma_lane_f64
 * [x] vfmaq_lane_f64
 * [x] vfmas_lane_f32
 * [x] vfmad_lane_f64
 * [x] vfma_laneq_f32
 * [x] vfmaq_laneq_f32
 * [x] vfma_laneq_f64
 * [x] vfmaq_laneq_f64
 * [x] vfmas_laneq_f32
 * [x] vfmad_laneq_f64
 * [ ] vfma_lane_f16
 * [ ] vfmaq_lane_f16
 * [ ] vfma_laneq_f16
 * [ ] vfmaq_laneq_f16

### fma_n

SIMDe currently implements 6 of 9 (66.67%) functions.

 * [x] vfma_n_f32
 * [x] vfma_n_f64
 * [ ] vfma_n_f16
 * [x] vfma_n_f32
 * [x] vfmaq_n_f32
 * [x] vfma_n_f64
 * [x] vfmaq_n_f64
 * [ ] vfma_n_f16
 * [ ] vfmaq_n_f16

### ld1_dup

SIMDe currently implements 31 of 33 (93.94%) functions, not counting 12 which require currently unsupported types.

 * [x] vld1_dup_s8
 * [x] vld1_dup_s16
 * [x] vld1_dup_s32
 * [x] vld1_dup_s64
 * [x] vld1_dup_u8
 * [x] vld1_dup_u16
 * [x] vld1_dup_u32
 * [x] vld1_dup_u64
 * [ ] vld1_dup_f16
 * [x] vld1_dup_f32
 * [x] vld1_dup_f64
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
 * [ ] vld1_dup_f16
 * [x] vld1q_dup_f16
 * [x] vld1_dup_f32
 * [x] vld1q_dup_f32
 * [x] vld1_dup_f64
 * [x] vld1q_dup_f64

### ld1_lane

SIMDe currently implements 30 of 33 (90.91%) functions, not counting 12 which require currently unsupported types.

 * [x] vld1_lane_s8
 * [x] vld1_lane_s16
 * [x] vld1_lane_s32
 * [x] vld1_lane_s64
 * [x] vld1_lane_u8
 * [x] vld1_lane_u16
 * [x] vld1_lane_u32
 * [x] vld1_lane_u64
 * [ ] vld1_lane_f16
 * [x] vld1_lane_f32
 * [x] vld1_lane_f64
 * [x] vld1_lane_s8
 * [x] vld1q_lane_s8
 * [x] vld1_lane_s16
 * [x] vld1q_lane_s16
 * [x] vld1_lane_s32
 * [x] vld1q_lane_s32
 * [x] vld1_lane_s64
 * [x] vld1q_lane_s64
 * [x] vld1_lane_u8
 * [x] vld1q_lane_u8
 * [x] vld1_lane_u16
 * [x] vld1q_lane_u16
 * [x] vld1_lane_u32
 * [x] vld1q_lane_u32
 * [x] vld1_lane_u64
 * [x] vld1q_lane_u64
 * [ ] vld1_lane_f16
 * [ ] vld1q_lane_f16
 * [x] vld1_lane_f32
 * [x] vld1q_lane_f32
 * [x] vld1_lane_f64
 * [x] vld1q_lane_f64

### ld1_x2

SIMDe currently implements 30 of 33 (90.91%) functions, not counting 12 which require currently unsupported types.

 * [x] vld1_s8_x2
 * [x] vld1_s16_x2
 * [x] vld1_s32_x2
 * [x] vld1_u8_x2
 * [x] vld1_u16_x2
 * [x] vld1_u32_x2
 * [ ] vld1_f16_x2
 * [x] vld1_f32_x2
 * [x] vld1_s64_x2
 * [x] vld1_u64_x2
 * [x] vld1_f64_x2
 * [x] vld1_s8_x2
 * [x] vld1q_s8_x2
 * [x] vld1_s16_x2
 * [x] vld1q_s16_x2
 * [x] vld1_s32_x2
 * [x] vld1q_s32_x2
 * [x] vld1_u8_x2
 * [x] vld1q_u8_x2
 * [x] vld1_u16_x2
 * [x] vld1q_u16_x2
 * [x] vld1_u32_x2
 * [x] vld1q_u32_x2
 * [ ] vld1_f16_x2
 * [ ] vld1q_f16_x2
 * [x] vld1_f32_x2
 * [x] vld1q_f32_x2
 * [x] vld1_s64_x2
 * [x] vld1_u64_x2
 * [x] vld1q_s64_x2
 * [x] vld1q_u64_x2
 * [x] vld1_f64_x2
 * [x] vld1q_f64_x2

### ld1_x3

SIMDe currently implements 30 of 33 (90.91%) functions, not counting 12 which require currently unsupported types.

 * [x] vld1_s8_x3
 * [x] vld1_s16_x3
 * [x] vld1_s32_x3
 * [x] vld1_u8_x3
 * [x] vld1_u16_x3
 * [x] vld1_u32_x3
 * [ ] vld1_f16_x3
 * [x] vld1_f32_x3
 * [x] vld1_s64_x3
 * [x] vld1_u64_x3
 * [x] vld1_f64_x3
 * [x] vld1_s8_x3
 * [x] vld1q_s8_x3
 * [x] vld1_s16_x3
 * [x] vld1q_s16_x3
 * [x] vld1_s32_x3
 * [x] vld1q_s32_x3
 * [x] vld1_u8_x3
 * [x] vld1q_u8_x3
 * [x] vld1_u16_x3
 * [x] vld1q_u16_x3
 * [x] vld1_u32_x3
 * [x] vld1q_u32_x3
 * [ ] vld1_f16_x3
 * [ ] vld1q_f16_x3
 * [x] vld1_f32_x3
 * [x] vld1q_f32_x3
 * [x] vld1_s64_x3
 * [x] vld1_u64_x3
 * [x] vld1q_s64_x3
 * [x] vld1q_u64_x3
 * [x] vld1_f64_x3
 * [x] vld1q_f64_x3

### ld1_x4

SIMDe currently implements 30 of 33 (90.91%) functions, not counting 12 which require currently unsupported types.

 * [x] vld1_s8_x4
 * [x] vld1_s16_x4
 * [x] vld1_s32_x4
 * [x] vld1_u8_x4
 * [x] vld1_u16_x4
 * [x] vld1_u32_x4
 * [ ] vld1_f16_x4
 * [x] vld1_f32_x4
 * [x] vld1_s64_x4
 * [x] vld1_u64_x4
 * [x] vld1_f64_x4
 * [x] vld1_s8_x4
 * [x] vld1q_s8_x4
 * [x] vld1_s16_x4
 * [x] vld1q_s16_x4
 * [x] vld1_s32_x4
 * [x] vld1q_s32_x4
 * [x] vld1_u8_x4
 * [x] vld1q_u8_x4
 * [x] vld1_u16_x4
 * [x] vld1q_u16_x4
 * [x] vld1_u32_x4
 * [x] vld1q_u32_x4
 * [ ] vld1_f16_x4
 * [ ] vld1q_f16_x4
 * [x] vld1_f32_x4
 * [x] vld1q_f32_x4
 * [x] vld1_s64_x4
 * [x] vld1_u64_x4
 * [x] vld1q_s64_x4
 * [x] vld1q_u64_x4
 * [x] vld1_f64_x4
 * [x] vld1q_f64_x4

### ld2

SIMDe currently implements 31 of 33 (93.94%) functions, not counting 12 which require currently unsupported types.

 * [x] vld2_s8
 * [x] vld2_s16
 * [x] vld2_s32
 * [x] vld2_u8
 * [x] vld2_u16
 * [x] vld2_u32
 * [ ] vld2_f16
 * [x] vld2_f32
 * [x] vld2_s64
 * [x] vld2_u64
 * [x] vld2_f64
 * [x] vld2_s8
 * [x] vld2q_s8
 * [x] vld2_s16
 * [x] vld2q_s16
 * [x] vld2_s32
 * [x] vld2q_s32
 * [x] vld2_u8
 * [x] vld2q_u8
 * [x] vld2_u16
 * [x] vld2q_u16
 * [x] vld2_u32
 * [x] vld2q_u32
 * [ ] vld2_f16
 * [x] vld2q_f16
 * [x] vld2_f32
 * [x] vld2q_f32
 * [x] vld2_s64
 * [x] vld2_u64
 * [x] vld2q_s64
 * [x] vld2q_u64
 * [x] vld2_f64
 * [x] vld2q_f64

### ld3

SIMDe currently implements 30 of 33 (90.91%) functions, not counting 12 which require currently unsupported types.

 * [x] vld3_s8
 * [x] vld3_s16
 * [x] vld3_s32
 * [x] vld3_u8
 * [x] vld3_u16
 * [x] vld3_u32
 * [ ] vld3_f16
 * [x] vld3_f32
 * [x] vld3_s64
 * [x] vld3_u64
 * [x] vld3_f64
 * [x] vld3_s8
 * [x] vld3q_s8
 * [x] vld3_s16
 * [x] vld3q_s16
 * [x] vld3_s32
 * [x] vld3q_s32
 * [x] vld3_u8
 * [x] vld3q_u8
 * [x] vld3_u16
 * [x] vld3q_u16
 * [x] vld3_u32
 * [x] vld3q_u32
 * [ ] vld3_f16
 * [ ] vld3q_f16
 * [x] vld3_f32
 * [x] vld3q_f32
 * [x] vld3_s64
 * [x] vld3_u64
 * [x] vld3q_s64
 * [x] vld3q_u64
 * [x] vld3_f64
 * [x] vld3q_f64

### ld4

SIMDe currently implements 30 of 33 (90.91%) functions, not counting 12 which require currently unsupported types.

 * [x] vld4_s8
 * [x] vld4_s16
 * [x] vld4_s32
 * [x] vld4_u8
 * [x] vld4_u16
 * [x] vld4_u32
 * [ ] vld4_f16
 * [x] vld4_f32
 * [x] vld4_s64
 * [x] vld4_u64
 * [x] vld4_f64
 * [x] vld4_s8
 * [x] vld4q_s8
 * [x] vld4_s16
 * [x] vld4q_s16
 * [x] vld4_s32
 * [x] vld4q_s32
 * [x] vld4_u8
 * [x] vld4q_u8
 * [x] vld4_u16
 * [x] vld4q_u16
 * [x] vld4_u32
 * [x] vld4q_u32
 * [ ] vld4_f16
 * [ ] vld4q_f16
 * [x] vld4_f32
 * [x] vld4q_f32
 * [x] vld4_s64
 * [x] vld4_u64
 * [x] vld4q_s64
 * [x] vld4q_u64
 * [x] vld4_f64
 * [x] vld4q_f64

### ld4_lane

SIMDe currently implements 30 of 33 (90.91%) functions, not counting 12 which require currently unsupported types.

 * [x] vld4_lane_s16
 * [x] vld4_lane_s32
 * [x] vld4_lane_u16
 * [x] vld4_lane_u32
 * [ ] vld4_lane_f16
 * [x] vld4_lane_f32
 * [x] vld4_lane_s8
 * [x] vld4_lane_u8
 * [x] vld4_lane_s64
 * [x] vld4_lane_u64
 * [x] vld4_lane_f64
 * [x] vld4_lane_s16
 * [x] vld4q_lane_s16
 * [x] vld4_lane_s32
 * [x] vld4q_lane_s32
 * [x] vld4_lane_u16
 * [x] vld4q_lane_u16
 * [x] vld4_lane_u32
 * [x] vld4q_lane_u32
 * [ ] vld4_lane_f16
 * [ ] vld4q_lane_f16
 * [x] vld4_lane_f32
 * [x] vld4q_lane_f32
 * [x] vld4_lane_s8
 * [x] vld4_lane_u8
 * [x] vld4q_lane_s8
 * [x] vld4q_lane_u8
 * [x] vld4_lane_s64
 * [x] vld4q_lane_s64
 * [x] vld4_lane_u64
 * [x] vld4q_lane_u64
 * [x] vld4_lane_f64
 * [x] vld4q_lane_f64

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

### mla_lane

SIMDe currently implements 15 of 30 (50.00%) functions.

 * [x] vmla_lane_s16
 * [x] vmla_lane_s32
 * [x] vmla_lane_u16
 * [x] vmla_lane_u32
 * [x] vmla_lane_f32
 * [ ] vmla_laneq_s16
 * [ ] vmla_laneq_s32
 * [ ] vmla_laneq_u16
 * [ ] vmla_laneq_u32
 * [ ] vmla_laneq_f32
 * [x] vmla_lane_s16
 * [x] vmlaq_lane_s16
 * [x] vmla_lane_s32
 * [x] vmlaq_lane_s32
 * [x] vmla_lane_u16
 * [x] vmlaq_lane_u16
 * [x] vmla_lane_u32
 * [x] vmlaq_lane_u32
 * [x] vmla_lane_f32
 * [x] vmlaq_lane_f32
 * [ ] vmla_laneq_s16
 * [ ] vmlaq_laneq_s16
 * [ ] vmla_laneq_s32
 * [ ] vmlaq_laneq_s32
 * [ ] vmla_laneq_u16
 * [ ] vmlaq_laneq_u16
 * [ ] vmla_laneq_u32
 * [ ] vmlaq_laneq_u32
 * [ ] vmla_laneq_f32
 * [ ] vmlaq_laneq_f32

### mul_lane

SIMDe currently implements 41 of 46 (89.13%) functions.

 * [x] vmul_lane_s16
 * [x] vmul_lane_s32
 * [x] vmul_lane_u16
 * [x] vmul_lane_u32
 * [x] vmul_lane_f32
 * [x] vmul_lane_f64
 * [x] vmul_laneq_s16
 * [x] vmul_laneq_s32
 * [x] vmul_laneq_u16
 * [x] vmul_laneq_u32
 * [x] vmul_laneq_f32
 * [x] vmul_laneq_f64
 * [ ] vmul_lane_f16
 * [ ] vmul_laneq_f16
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
 * [x] vmul_laneq_s16
 * [x] vmulq_laneq_s16
 * [x] vmul_laneq_s32
 * [x] vmulq_laneq_s32
 * [x] vmul_laneq_u16
 * [x] vmulq_laneq_u16
 * [x] vmul_laneq_u32
 * [x] vmulq_laneq_u32
 * [x] vmul_laneq_f32
 * [x] vmulq_laneq_f32
 * [x] vmul_laneq_f64
 * [x] vmulq_laneq_f64
 * [x] vmuls_laneq_f32
 * [x] vmuld_laneq_f64
 * [ ] vmul_lane_f16
 * [x] vmulq_lane_f16
 * [ ] vmul_laneq_f16
 * [ ] vmulq_laneq_f16

### neg

SIMDe currently implements 19 of 22 (86.36%) functions.

 * [x] vneg_s8
 * [x] vneg_s16
 * [x] vneg_s32
 * [x] vneg_f32
 * [x] vneg_s64
 * [x] vneg_f64
 * [ ] vneg_f16
 * [x] vneg_s8
 * [x] vnegq_s8
 * [x] vneg_s16
 * [x] vnegq_s16
 * [x] vneg_s32
 * [x] vnegq_s32
 * [x] vneg_f32
 * [x] vnegq_f32
 * [x] vneg_s64
 * [x] vnegd_s64
 * [x] vnegq_s64
 * [x] vneg_f64
 * [x] vnegq_f64
 * [ ] vneg_f16
 * [ ] vnegq_f16

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

### reinterpret

SIMDe currently implements 300 of 330 (90.91%) functions, not counting 316 which require currently unsupported types.

 * [x] vreinterpret_s16_s8
 * [x] vreinterpret_s32_s8
 * [x] vreinterpret_f32_s8
 * [x] vreinterpret_u8_s8
 * [x] vreinterpret_u16_s8
 * [x] vreinterpret_u32_s8
 * [x] vreinterpret_u64_s8
 * [x] vreinterpret_s64_s8
 * [x] vreinterpret_f64_s8
 * [x] vreinterpret_f16_s8
 * [x] vreinterpret_s8_s16
 * [x] vreinterpret_s32_s16
 * [x] vreinterpret_f32_s16
 * [x] vreinterpret_u8_s16
 * [x] vreinterpret_u16_s16
 * [x] vreinterpret_u32_s16
 * [x] vreinterpret_u64_s16
 * [x] vreinterpret_s64_s16
 * [x] vreinterpret_f64_s16
 * [x] vreinterpret_f16_s16
 * [x] vreinterpret_s8_s32
 * [x] vreinterpret_s16_s32
 * [x] vreinterpret_f32_s32
 * [x] vreinterpret_u8_s32
 * [x] vreinterpret_u16_s32
 * [x] vreinterpret_u32_s32
 * [x] vreinterpret_u64_s32
 * [x] vreinterpret_s64_s32
 * [x] vreinterpret_f64_s32
 * [x] vreinterpret_f16_s32
 * [x] vreinterpret_s8_f32
 * [x] vreinterpret_s16_f32
 * [x] vreinterpret_s32_f32
 * [x] vreinterpret_u8_f32
 * [x] vreinterpret_u16_f32
 * [x] vreinterpret_u32_f32
 * [x] vreinterpret_u64_f32
 * [x] vreinterpret_s64_f32
 * [x] vreinterpret_f64_f32
 * [x] vreinterpret_f16_f32
 * [x] vreinterpret_s8_u8
 * [x] vreinterpret_s16_u8
 * [x] vreinterpret_s32_u8
 * [x] vreinterpret_f32_u8
 * [x] vreinterpret_u16_u8
 * [x] vreinterpret_u32_u8
 * [x] vreinterpret_u64_u8
 * [x] vreinterpret_s64_u8
 * [x] vreinterpret_f64_u8
 * [x] vreinterpret_f16_u8
 * [x] vreinterpret_s8_u16
 * [x] vreinterpret_s16_u16
 * [x] vreinterpret_s32_u16
 * [x] vreinterpret_f32_u16
 * [x] vreinterpret_u8_u16
 * [x] vreinterpret_u32_u16
 * [x] vreinterpret_u64_u16
 * [x] vreinterpret_s64_u16
 * [x] vreinterpret_f64_u16
 * [x] vreinterpret_f16_u16
 * [x] vreinterpret_s8_u32
 * [x] vreinterpret_s16_u32
 * [x] vreinterpret_s32_u32
 * [x] vreinterpret_f32_u32
 * [x] vreinterpret_u8_u32
 * [x] vreinterpret_u16_u32
 * [x] vreinterpret_u64_u32
 * [x] vreinterpret_s64_u32
 * [x] vreinterpret_f64_u32
 * [x] vreinterpret_f16_u32
 * [x] vreinterpret_s8_u64
 * [x] vreinterpret_s16_u64
 * [x] vreinterpret_s32_u64
 * [x] vreinterpret_f32_u64
 * [x] vreinterpret_u8_u64
 * [x] vreinterpret_u16_u64
 * [x] vreinterpret_u32_u64
 * [x] vreinterpret_s64_u64
 * [x] vreinterpret_f64_u64
 * [x] vreinterpret_f16_u64
 * [x] vreinterpret_s8_s64
 * [x] vreinterpret_s16_s64
 * [x] vreinterpret_s32_s64
 * [x] vreinterpret_f32_s64
 * [x] vreinterpret_u8_s64
 * [x] vreinterpret_u16_s64
 * [x] vreinterpret_u32_s64
 * [x] vreinterpret_u64_s64
 * [x] vreinterpret_f64_s64
 * [x] vreinterpret_f16_s64
 * [ ] vreinterpret_s8_f16
 * [ ] vreinterpret_s16_f16
 * [ ] vreinterpret_s32_f16
 * [ ] vreinterpret_f32_f16
 * [ ] vreinterpret_u8_f16
 * [x] vreinterpret_u16_f16
 * [ ] vreinterpret_u32_f16
 * [ ] vreinterpret_u64_f16
 * [ ] vreinterpret_s64_f16
 * [ ] vreinterpret_f64_f16
 * [x] vreinterpret_s8_f64
 * [x] vreinterpret_s16_f64
 * [x] vreinterpret_s32_f64
 * [x] vreinterpret_u8_f64
 * [x] vreinterpret_u16_f64
 * [x] vreinterpret_u32_f64
 * [x] vreinterpret_u64_f64
 * [x] vreinterpret_s64_f64
 * [ ] vreinterpret_f16_f64
 * [x] vreinterpret_f32_f64
 * [x] vreinterpret_s16_s8
 * [x] vreinterpret_s32_s8
 * [x] vreinterpret_f32_s8
 * [x] vreinterpret_u8_s8
 * [x] vreinterpret_u16_s8
 * [x] vreinterpret_u32_s8
 * [x] vreinterpret_u64_s8
 * [x] vreinterpret_s64_s8
 * [x] vreinterpret_f64_s8
 * [x] vreinterpret_f16_s8
 * [x] vreinterpret_s8_s16
 * [x] vreinterpret_s32_s16
 * [x] vreinterpret_f32_s16
 * [x] vreinterpret_u8_s16
 * [x] vreinterpret_u16_s16
 * [x] vreinterpret_u32_s16
 * [x] vreinterpret_u64_s16
 * [x] vreinterpret_s64_s16
 * [x] vreinterpret_f64_s16
 * [x] vreinterpret_f16_s16
 * [x] vreinterpret_s8_s32
 * [x] vreinterpret_s16_s32
 * [x] vreinterpret_f32_s32
 * [x] vreinterpret_u8_s32
 * [x] vreinterpret_u16_s32
 * [x] vreinterpret_u32_s32
 * [x] vreinterpret_u64_s32
 * [x] vreinterpret_s64_s32
 * [x] vreinterpret_f64_s32
 * [x] vreinterpret_f16_s32
 * [x] vreinterpret_s8_f32
 * [x] vreinterpret_s16_f32
 * [x] vreinterpret_s32_f32
 * [x] vreinterpret_u8_f32
 * [x] vreinterpret_u16_f32
 * [x] vreinterpret_u32_f32
 * [x] vreinterpret_u64_f32
 * [x] vreinterpret_s64_f32
 * [x] vreinterpret_f64_f32
 * [x] vreinterpret_f16_f32
 * [x] vreinterpret_s8_u8
 * [x] vreinterpret_s16_u8
 * [x] vreinterpret_s32_u8
 * [x] vreinterpret_f32_u8
 * [x] vreinterpret_u16_u8
 * [x] vreinterpret_u32_u8
 * [x] vreinterpret_u64_u8
 * [x] vreinterpret_s64_u8
 * [x] vreinterpret_f64_u8
 * [x] vreinterpret_f16_u8
 * [x] vreinterpret_s8_u16
 * [x] vreinterpret_s16_u16
 * [x] vreinterpret_s32_u16
 * [x] vreinterpret_f32_u16
 * [x] vreinterpret_u8_u16
 * [x] vreinterpret_u32_u16
 * [x] vreinterpret_u64_u16
 * [x] vreinterpret_s64_u16
 * [x] vreinterpret_f64_u16
 * [x] vreinterpret_f16_u16
 * [x] vreinterpret_s8_u32
 * [x] vreinterpret_s16_u32
 * [x] vreinterpret_s32_u32
 * [x] vreinterpret_f32_u32
 * [x] vreinterpret_u8_u32
 * [x] vreinterpret_u16_u32
 * [x] vreinterpret_u64_u32
 * [x] vreinterpret_s64_u32
 * [x] vreinterpret_f64_u32
 * [x] vreinterpret_f16_u32
 * [x] vreinterpret_s8_u64
 * [x] vreinterpret_s16_u64
 * [x] vreinterpret_s32_u64
 * [x] vreinterpret_f32_u64
 * [x] vreinterpret_u8_u64
 * [x] vreinterpret_u16_u64
 * [x] vreinterpret_u32_u64
 * [x] vreinterpret_s64_u64
 * [x] vreinterpret_f64_u64
 * [x] vreinterpret_f16_u64
 * [x] vreinterpret_s8_s64
 * [x] vreinterpret_s16_s64
 * [x] vreinterpret_s32_s64
 * [x] vreinterpret_f32_s64
 * [x] vreinterpret_u8_s64
 * [x] vreinterpret_u16_s64
 * [x] vreinterpret_u32_s64
 * [x] vreinterpret_u64_s64
 * [x] vreinterpret_f64_s64
 * [x] vreinterpret_f16_s64
 * [ ] vreinterpret_s8_f16
 * [ ] vreinterpret_s16_f16
 * [ ] vreinterpret_s32_f16
 * [ ] vreinterpret_f32_f16
 * [ ] vreinterpret_u8_f16
 * [x] vreinterpret_u16_f16
 * [ ] vreinterpret_u32_f16
 * [ ] vreinterpret_u64_f16
 * [ ] vreinterpret_s64_f16
 * [ ] vreinterpret_f64_f16
 * [x] vreinterpretq_s16_s8
 * [x] vreinterpretq_s32_s8
 * [x] vreinterpretq_f32_s8
 * [x] vreinterpretq_u8_s8
 * [x] vreinterpretq_u16_s8
 * [x] vreinterpretq_u32_s8
 * [x] vreinterpretq_u64_s8
 * [x] vreinterpretq_s64_s8
 * [x] vreinterpretq_f64_s8
 * [x] vreinterpretq_f16_s8
 * [x] vreinterpretq_s8_s16
 * [x] vreinterpretq_s32_s16
 * [x] vreinterpretq_f32_s16
 * [x] vreinterpretq_u8_s16
 * [x] vreinterpretq_u16_s16
 * [x] vreinterpretq_u32_s16
 * [x] vreinterpretq_u64_s16
 * [x] vreinterpretq_s64_s16
 * [x] vreinterpretq_f64_s16
 * [x] vreinterpretq_f16_s16
 * [x] vreinterpretq_s8_s32
 * [x] vreinterpretq_s16_s32
 * [x] vreinterpretq_f32_s32
 * [x] vreinterpretq_u8_s32
 * [x] vreinterpretq_u16_s32
 * [x] vreinterpretq_u32_s32
 * [x] vreinterpretq_u64_s32
 * [x] vreinterpretq_s64_s32
 * [x] vreinterpretq_f64_s32
 * [x] vreinterpretq_f16_s32
 * [x] vreinterpretq_s8_f32
 * [x] vreinterpretq_s16_f32
 * [x] vreinterpretq_s32_f32
 * [x] vreinterpretq_u8_f32
 * [x] vreinterpretq_u16_f32
 * [x] vreinterpretq_u32_f32
 * [x] vreinterpretq_u64_f32
 * [x] vreinterpretq_s64_f32
 * [x] vreinterpretq_f64_f32
 * [x] vreinterpretq_f16_f32
 * [x] vreinterpretq_s8_u8
 * [x] vreinterpretq_s16_u8
 * [x] vreinterpretq_s32_u8
 * [x] vreinterpretq_f32_u8
 * [x] vreinterpretq_u16_u8
 * [x] vreinterpretq_u32_u8
 * [x] vreinterpretq_u64_u8
 * [x] vreinterpretq_s64_u8
 * [x] vreinterpretq_f64_u8
 * [x] vreinterpretq_f16_u8
 * [x] vreinterpretq_s8_u16
 * [x] vreinterpretq_s16_u16
 * [x] vreinterpretq_s32_u16
 * [x] vreinterpretq_f32_u16
 * [x] vreinterpretq_u8_u16
 * [x] vreinterpretq_u32_u16
 * [x] vreinterpretq_u64_u16
 * [x] vreinterpretq_s64_u16
 * [x] vreinterpretq_f64_u16
 * [x] vreinterpretq_f16_u16
 * [x] vreinterpretq_s8_u32
 * [x] vreinterpretq_s16_u32
 * [x] vreinterpretq_s32_u32
 * [x] vreinterpretq_f32_u32
 * [x] vreinterpretq_u8_u32
 * [x] vreinterpretq_u16_u32
 * [x] vreinterpretq_u64_u32
 * [x] vreinterpretq_s64_u32
 * [x] vreinterpretq_f64_u32
 * [x] vreinterpretq_f16_u32
 * [x] vreinterpretq_s8_u64
 * [x] vreinterpretq_s16_u64
 * [x] vreinterpretq_s32_u64
 * [x] vreinterpretq_f32_u64
 * [x] vreinterpretq_u8_u64
 * [x] vreinterpretq_u16_u64
 * [x] vreinterpretq_u32_u64
 * [x] vreinterpretq_s64_u64
 * [x] vreinterpretq_f64_u64
 * [x] vreinterpretq_f64_s64
 * [x] vreinterpretq_f16_u64
 * [x] vreinterpretq_s8_s64
 * [x] vreinterpretq_s16_s64
 * [x] vreinterpretq_s32_s64
 * [x] vreinterpretq_f32_s64
 * [x] vreinterpretq_u8_s64
 * [x] vreinterpretq_u16_s64
 * [x] vreinterpretq_u32_s64
 * [x] vreinterpretq_u64_s64
 * [x] vreinterpretq_f16_s64
 * [ ] vreinterpretq_s8_f16
 * [ ] vreinterpretq_s16_f16
 * [ ] vreinterpretq_s32_f16
 * [ ] vreinterpretq_f32_f16
 * [ ] vreinterpretq_u8_f16
 * [x] vreinterpretq_u16_f16
 * [ ] vreinterpretq_u32_f16
 * [ ] vreinterpretq_u64_f16
 * [ ] vreinterpretq_s64_f16
 * [ ] vreinterpretq_f64_f16
 * [x] vreinterpret_s8_f64
 * [x] vreinterpret_s16_f64
 * [x] vreinterpret_s32_f64
 * [x] vreinterpret_u8_f64
 * [x] vreinterpret_u16_f64
 * [x] vreinterpret_u32_f64
 * [x] vreinterpret_u64_f64
 * [x] vreinterpret_s64_f64
 * [ ] vreinterpret_f16_f64
 * [x] vreinterpret_f32_f64
 * [x] vreinterpretq_s8_f64
 * [x] vreinterpretq_s16_f64
 * [x] vreinterpretq_s32_f64
 * [x] vreinterpretq_u8_f64
 * [x] vreinterpretq_u16_f64
 * [x] vreinterpretq_u32_f64
 * [x] vreinterpretq_u64_f64
 * [x] vreinterpretq_s64_f64
 * [ ] vreinterpretq_f16_f64
 * [x] vreinterpretq_f32_f64

### rev64

SIMDe currently implements 21 of 24 (87.50%) functions, not counting 6 which require currently unsupported types.

 * [x] vrev64_s8
 * [x] vrev64_s16
 * [x] vrev64_s32
 * [x] vrev64_u8
 * [x] vrev64_u16
 * [x] vrev64_u32
 * [x] vrev64_f32
 * [ ] vrev64_f16
 * [x] vrev64_s8
 * [x] vrev64q_s8
 * [x] vrev64_s16
 * [x] vrev64q_s16
 * [x] vrev64_s32
 * [x] vrev64q_s32
 * [x] vrev64_u8
 * [x] vrev64q_u8
 * [x] vrev64_u16
 * [x] vrev64q_u16
 * [x] vrev64_u32
 * [x] vrev64q_u32
 * [x] vrev64_f32
 * [x] vrev64q_f32
 * [ ] vrev64_f16
 * [ ] vrev64q_f16

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

### st1_lane

SIMDe currently implements 30 of 33 (90.91%) functions, not counting 12 which require currently unsupported types.

 * [x] vst1_lane_s8
 * [x] vst1_lane_s16
 * [x] vst1_lane_s32
 * [x] vst1_lane_s64
 * [x] vst1_lane_u8
 * [x] vst1_lane_u16
 * [x] vst1_lane_u32
 * [x] vst1_lane_u64
 * [ ] vst1_lane_f16
 * [x] vst1_lane_f32
 * [x] vst1_lane_f64
 * [x] vst1_lane_s8
 * [x] vst1q_lane_s8
 * [x] vst1_lane_s16
 * [x] vst1q_lane_s16
 * [x] vst1_lane_s32
 * [x] vst1q_lane_s32
 * [x] vst1_lane_s64
 * [x] vst1q_lane_s64
 * [x] vst1_lane_u8
 * [x] vst1q_lane_u8
 * [x] vst1_lane_u16
 * [x] vst1q_lane_u16
 * [x] vst1_lane_u32
 * [x] vst1q_lane_u32
 * [x] vst1_lane_u64
 * [x] vst1q_lane_u64
 * [ ] vst1_lane_f16
 * [ ] vst1q_lane_f16
 * [x] vst1_lane_f32
 * [x] vst1q_lane_f32
 * [x] vst1_lane_f64
 * [x] vst1q_lane_f64

### st2_lane

SIMDe currently implements 30 of 33 (90.91%) functions, not counting 12 which require currently unsupported types.

 * [x] vst2_lane_s8
 * [x] vst2_lane_u8
 * [x] vst2_lane_s16
 * [x] vst2_lane_s32
 * [x] vst2_lane_u16
 * [x] vst2_lane_u32
 * [ ] vst2_lane_f16
 * [x] vst2_lane_f32
 * [x] vst2_lane_s64
 * [x] vst2_lane_u64
 * [x] vst2_lane_f64
 * [x] vst2_lane_s8
 * [x] vst2_lane_u8
 * [x] vst2_lane_s16
 * [x] vst2q_lane_s16
 * [x] vst2_lane_s32
 * [x] vst2q_lane_s32
 * [x] vst2_lane_u16
 * [x] vst2q_lane_u16
 * [x] vst2_lane_u32
 * [x] vst2q_lane_u32
 * [ ] vst2_lane_f16
 * [ ] vst2q_lane_f16
 * [x] vst2_lane_f32
 * [x] vst2q_lane_f32
 * [x] vst2q_lane_s8
 * [x] vst2q_lane_u8
 * [x] vst2_lane_s64
 * [x] vst2q_lane_s64
 * [x] vst2_lane_u64
 * [x] vst2q_lane_u64
 * [x] vst2_lane_f64
 * [x] vst2q_lane_f64

### st3

SIMDe currently implements 30 of 33 (90.91%) functions, not counting 12 which require currently unsupported types.

 * [x] vst3_s8
 * [x] vst3_s16
 * [x] vst3_s32
 * [x] vst3_u8
 * [x] vst3_u16
 * [x] vst3_u32
 * [ ] vst3_f16
 * [x] vst3_f32
 * [x] vst3_s64
 * [x] vst3_u64
 * [x] vst3_f64
 * [x] vst3_s8
 * [x] vst3q_s8
 * [x] vst3_s16
 * [x] vst3q_s16
 * [x] vst3_s32
 * [x] vst3q_s32
 * [x] vst3_u8
 * [x] vst3q_u8
 * [x] vst3_u16
 * [x] vst3q_u16
 * [x] vst3_u32
 * [x] vst3q_u32
 * [ ] vst3_f16
 * [ ] vst3q_f16
 * [x] vst3_f32
 * [x] vst3q_f32
 * [x] vst3_s64
 * [x] vst3_u64
 * [x] vst3q_s64
 * [x] vst3q_u64
 * [x] vst3_f64
 * [x] vst3q_f64

### st3_lane

SIMDe currently implements 30 of 33 (90.91%) functions, not counting 12 which require currently unsupported types.

 * [x] vst3_lane_s8
 * [x] vst3_lane_u8
 * [x] vst3_lane_s16
 * [x] vst3_lane_s32
 * [x] vst3_lane_u16
 * [x] vst3_lane_u32
 * [ ] vst3_lane_f16
 * [x] vst3_lane_f32
 * [x] vst3_lane_s64
 * [x] vst3_lane_u64
 * [x] vst3_lane_f64
 * [x] vst3_lane_s8
 * [x] vst3_lane_u8
 * [x] vst3_lane_s16
 * [x] vst3q_lane_s16
 * [x] vst3_lane_s32
 * [x] vst3q_lane_s32
 * [x] vst3_lane_u16
 * [x] vst3q_lane_u16
 * [x] vst3_lane_u32
 * [x] vst3q_lane_u32
 * [ ] vst3_lane_f16
 * [ ] vst3q_lane_f16
 * [x] vst3_lane_f32
 * [x] vst3q_lane_f32
 * [x] vst3q_lane_s8
 * [x] vst3q_lane_u8
 * [x] vst3_lane_s64
 * [x] vst3q_lane_s64
 * [x] vst3_lane_u64
 * [x] vst3q_lane_u64
 * [x] vst3_lane_f64
 * [x] vst3q_lane_f64

### st4

SIMDe currently implements 30 of 33 (90.91%) functions, not counting 12 which require currently unsupported types.

 * [x] vst4_s8
 * [x] vst4_s16
 * [x] vst4_s32
 * [x] vst4_u8
 * [x] vst4_u16
 * [x] vst4_u32
 * [ ] vst4_f16
 * [x] vst4_f32
 * [x] vst4_s64
 * [x] vst4_u64
 * [x] vst4_f64
 * [x] vst4_s8
 * [x] vst4q_s8
 * [x] vst4_s16
 * [x] vst4q_s16
 * [x] vst4_s32
 * [x] vst4q_s32
 * [x] vst4_u8
 * [x] vst4q_u8
 * [x] vst4_u16
 * [x] vst4q_u16
 * [x] vst4_u32
 * [x] vst4q_u32
 * [ ] vst4_f16
 * [ ] vst4q_f16
 * [x] vst4_f32
 * [x] vst4q_f32
 * [x] vst4_s64
 * [x] vst4_u64
 * [x] vst4q_s64
 * [x] vst4q_u64
 * [x] vst4_f64
 * [x] vst4q_f64

### st4_lane

SIMDe currently implements 30 of 33 (90.91%) functions, not counting 12 which require currently unsupported types.

 * [x] vst4_lane_s8
 * [x] vst4_lane_u8
 * [x] vst4_lane_s16
 * [x] vst4_lane_s32
 * [x] vst4_lane_u16
 * [x] vst4_lane_u32
 * [ ] vst4_lane_f16
 * [x] vst4_lane_f32
 * [x] vst4_lane_s64
 * [x] vst4_lane_u64
 * [x] vst4_lane_f64
 * [x] vst4_lane_s8
 * [x] vst4_lane_u8
 * [x] vst4_lane_s16
 * [x] vst4q_lane_s16
 * [x] vst4_lane_s32
 * [x] vst4q_lane_s32
 * [x] vst4_lane_u16
 * [x] vst4q_lane_u16
 * [x] vst4_lane_u32
 * [x] vst4q_lane_u32
 * [ ] vst4_lane_f16
 * [ ] vst4q_lane_f16
 * [x] vst4_lane_f32
 * [x] vst4q_lane_f32
 * [x] vst4q_lane_s8
 * [x] vst4q_lane_u8
 * [x] vst4_lane_s64
 * [x] vst4q_lane_s64
 * [x] vst4_lane_u64
 * [x] vst4q_lane_u64
 * [x] vst4_lane_f64
 * [x] vst4q_lane_f64

### trn

SIMDe currently implements 21 of 24 (87.50%) functions, not counting 6 which require currently unsupported types.

 * [x] vtrn_s8
 * [x] vtrn_s16
 * [x] vtrn_u8
 * [x] vtrn_u16
 * [x] vtrn_s32
 * [x] vtrn_f32
 * [x] vtrn_u32
 * [ ] vtrn_f16
 * [x] vtrn_s8
 * [x] vtrn_s16
 * [x] vtrn_u8
 * [x] vtrn_u16
 * [x] vtrn_s32
 * [x] vtrn_f32
 * [x] vtrn_u32
 * [x] vtrnq_s8
 * [x] vtrnq_s16
 * [x] vtrnq_s32
 * [x] vtrnq_f32
 * [x] vtrnq_u8
 * [x] vtrnq_u16
 * [x] vtrnq_u32
 * [ ] vtrn_f16
 * [ ] vtrnq_f16

### trn1

SIMDe currently implements 24 of 27 (88.89%) functions, not counting 7 which require currently unsupported types.

 * [x] vtrn1_s8
 * [x] vtrn1_s16
 * [x] vtrn1_s32
 * [x] vtrn1_u8
 * [x] vtrn1_u16
 * [x] vtrn1_u32
 * [x] vtrn1_f32
 * [ ] vtrn1_f16
 * [x] vtrn1_s8
 * [x] vtrn1q_s8
 * [x] vtrn1_s16
 * [x] vtrn1q_s16
 * [x] vtrn1_s32
 * [x] vtrn1q_s32
 * [x] vtrn1q_s64
 * [x] vtrn1_u8
 * [x] vtrn1q_u8
 * [x] vtrn1_u16
 * [x] vtrn1q_u16
 * [x] vtrn1_u32
 * [x] vtrn1q_u32
 * [x] vtrn1q_u64
 * [x] vtrn1_f32
 * [x] vtrn1q_f32
 * [x] vtrn1q_f64
 * [ ] vtrn1_f16
 * [ ] vtrn1q_f16

### trn2

SIMDe currently implements 24 of 27 (88.89%) functions, not counting 7 which require currently unsupported types.

 * [x] vtrn2_s8
 * [x] vtrn2_s16
 * [x] vtrn2_s32
 * [x] vtrn2_u8
 * [x] vtrn2_u16
 * [x] vtrn2_u32
 * [x] vtrn2_f32
 * [ ] vtrn2_f16
 * [x] vtrn2_s8
 * [x] vtrn2q_s8
 * [x] vtrn2_s16
 * [x] vtrn2q_s16
 * [x] vtrn2_s32
 * [x] vtrn2q_s32
 * [x] vtrn2q_s64
 * [x] vtrn2_u8
 * [x] vtrn2q_u8
 * [x] vtrn2_u16
 * [x] vtrn2q_u16
 * [x] vtrn2_u32
 * [x] vtrn2q_u32
 * [x] vtrn2q_u64
 * [x] vtrn2_f32
 * [x] vtrn2q_f32
 * [x] vtrn2q_f64
 * [ ] vtrn2_f16
 * [ ] vtrn2q_f16

### uzp

SIMDe currently implements 21 of 24 (87.50%) functions, not counting 6 which require currently unsupported types.

 * [x] vuzp_s8
 * [x] vuzp_s16
 * [x] vuzp_s32
 * [x] vuzp_f32
 * [x] vuzp_u8
 * [x] vuzp_u16
 * [x] vuzp_u32
 * [ ] vuzp_f16
 * [x] vuzp_s8
 * [x] vuzp_s16
 * [x] vuzp_s32
 * [x] vuzp_f32
 * [x] vuzp_u8
 * [x] vuzp_u16
 * [x] vuzp_u32
 * [x] vuzpq_s8
 * [x] vuzpq_s16
 * [x] vuzpq_s32
 * [x] vuzpq_f32
 * [x] vuzpq_u8
 * [x] vuzpq_u16
 * [x] vuzpq_u32
 * [ ] vuzp_f16
 * [ ] vuzpq_f16

### uzp1

SIMDe currently implements 26 of 27 (96.30%) functions, not counting 7 which require currently unsupported types.

 * [x] vuzp1_s8
 * [x] vuzp1_s16
 * [x] vuzp1_s32
 * [x] vuzp1_u8
 * [x] vuzp1_u16
 * [x] vuzp1_u32
 * [x] vuzp1_f32
 * [x] vuzp1_f16
 * [x] vuzp1_s8
 * [x] vuzp1q_s8
 * [x] vuzp1_s16
 * [x] vuzp1q_s16
 * [x] vuzp1_s32
 * [x] vuzp1q_s32
 * [x] vuzp1q_s64
 * [x] vuzp1_u8
 * [x] vuzp1q_u8
 * [x] vuzp1_u16
 * [x] vuzp1q_u16
 * [x] vuzp1_u32
 * [x] vuzp1q_u32
 * [x] vuzp1q_u64
 * [x] vuzp1_f32
 * [x] vuzp1q_f32
 * [x] vuzp1q_f64
 * [x] vuzp1_f16
 * [ ] vuzp1q_f16

### uzp2

SIMDe currently implements 26 of 27 (96.30%) functions, not counting 7 which require currently unsupported types.

 * [x] vuzp2_s8
 * [x] vuzp2_s16
 * [x] vuzp2_s32
 * [x] vuzp2_u8
 * [x] vuzp2_u16
 * [x] vuzp2_u32
 * [x] vuzp2_f32
 * [x] vuzp2_f16
 * [x] vuzp2_s8
 * [x] vuzp2q_s8
 * [x] vuzp2_s16
 * [x] vuzp2q_s16
 * [x] vuzp2_s32
 * [x] vuzp2q_s32
 * [x] vuzp2q_s64
 * [x] vuzp2_u8
 * [x] vuzp2q_u8
 * [x] vuzp2_u16
 * [x] vuzp2q_u16
 * [x] vuzp2_u32
 * [x] vuzp2q_u32
 * [x] vuzp2q_u64
 * [x] vuzp2_f32
 * [x] vuzp2q_f32
 * [x] vuzp2q_f64
 * [x] vuzp2_f16
 * [ ] vuzp2q_f16

## Unimplemented Families

There are currently 53 unimplemented families.

 * abal (12 functions)
 * abal_high (12 functions)
 * abdh (2 functions)
 * abdl_high (12 functions)
 * addhn_high (12 functions)
 * aes (8 functions)
 * bfdot (3 functions)
 * bfdot_lane (6 functions)
 * cadd_rot (14 functions)
 * cale (11 functions)
 * caleh (2 functions)
 * calt (11 functions)
 * calth (2 functions)
 * cgezh (2 functions)
 * cgtzh (2 functions)
 * cleh (2 functions)
 * cltzh (2 functions)
 * cmla_lane (14 functions)
 * cmla_rot_lane (42 functions)
 * copy_lane (60 functions, plus 24 functions with unsupported types)
 * cvt_high (8 functions, plus 2 functions with unsupported types)
 * cvt_n (44 functions)
 * cvtah (12 functions, plus 2 functions with unsupported types)
 * cvth (24 functions, plus 2 functions with unsupported types)
 * cvth_n (24 functions)
 * cvtm (22 functions)
 * cvtmh (12 functions)
 * cvtnh (12 functions)
 * cvtp (22 functions)
 * cvtph (12 functions)
 * cvtx (3 functions)
 * cvtx_high (2 functions)
 * divh (2 functions)
 * dupb_lane (4 functions, plus 4 functions with unsupported types)
 * duph_lane (12 functions, plus 8 functions with unsupported types)
 * eor3 (9 functions)
 * fmah (2 functions)
 * fmah_lane (4 functions)
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
 * fms (8 functions)
 * fms_lane (20 functions)
 * fms_n (8 functions)
 * fmsh (2 functions)
 * fmsh_lane (4 functions)
 * ld2_dup (33 functions, plus 12 functions with unsupported types)
 * ld2_lane (33 functions, plus 12 functions with unsupported types)
 * ld3_dup (33 functions, plus 12 functions with unsupported types)
 * ld3_lane (33 functions, plus 12 functions with unsupported types)
 * ld4_dup (33 functions, plus 12 functions with unsupported types)
 * maxnmh (2 functions)
 * maxnmv (7 functions)
 * minnmh (2 functions)
 * minnmv (7 functions)
 * mlal_high_lane (16 functions)
 * mls_lane (24 functions)
 * mlsl_high_lane (16 functions)
 * mmla (7 functions)
 * mulh_lane (4 functions)
 * mull_high_lane (16 functions)
 * mull_high_n (8 functions)
 * mulx (11 functions)
 * mulx_lane (22 functions)
 * mulx_n (3 functions)
 * mulxh (2 functions)
 * mulxh_lane (4 functions)
 * negh (2 functions)
 * pmaxnm (10 functions)
 * pminnm (10 functions)
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
 * qrshrun_high_n (6 functions)
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
 * st1_x2 (33 functions, plus 12 functions with unsupported types)
 * st1_x3 (33 functions, plus 12 functions with unsupported types)
 * st1_x4 (33 functions, plus 12 functions with unsupported types)
 * subhn_high (12 functions)
 * sudot_lane (6 functions)
 * usdot (3 functions)
 * usdot_lane (6 functions)

## Complete Families

SIMDe contains complete implementations of 178 functions families.

 * aba
 * abdl
 * abs
 * absh
 * add (10 functions with unsupported types)
 * addh
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
 * bsl (9 functions with unsupported types)
 * cage
 * cageh
 * cagt
 * cagth
 * ceq (6 functions with unsupported types)
 * ceqh
 * ceqz (6 functions with unsupported types)
 * ceqzh
 * cge
 * cgeh
 * cgt
 * cgth
 * clez
 * clezh
 * cls
 * clt
 * clth
 * clz
 * cnt (3 functions with unsupported types)
 * combine (8 functions with unsupported types)
 * cvt (4 functions with unsupported types)
 * cvt_low (3 functions with unsupported types)
 * dot
 * dot_lane
 * dup_n (12 functions with unsupported types)
 * eor
 * get_high (8 functions with unsupported types)
 * get_lane (12 functions with unsupported types)
 * get_low (8 functions with unsupported types)
 * hadd
 * hsub
 * ld1 (12 functions with unsupported types)
 * ldr (2 functions with unsupported types)
 * max
 * maxh
 * min
 * minh
 * mla
 * mla_n
 * mlal
 * mlal_high
 * mlal_high_n
 * mlal_lane
 * mlal_n
 * mls
 * mls_n
 * mlsl
 * mlsl_high
 * mlsl_high_n
 * mlsl_lane
 * mlsl_n
 * mov_n (6 functions with unsupported types)
 * movl
 * movl_high
 * movn
 * movn_high
 * mul (3 functions with unsupported types)
 * mul_n
 * mulh
 * mull (4 functions with unsupported types)
 * mull_high (4 functions with unsupported types)
 * mull_lane
 * mull_n
 * mvn (3 functions with unsupported types)
 * orn
 * orr
 * padal
 * paddl
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
 * qrshrnh_n
 * qrshrun_n
 * qrshrunh_n
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
 * recpe
 * recpeh
 * recps
 * rev16 (3 functions with unsupported types)
 * rev32 (6 functions with unsupported types)
 * rhadd
 * rndn
 * rndnh
 * rshl
 * rshr_n
 * rshrn_n
 * rsqrte
 * rsqrteh
 * rsqrts
 * rsqrtsh
 * rsra_n
 * set_lane (12 functions with unsupported types)
 * shl
 * shl_n
 * shll_n
 * shr_n
 * shrn_n
 * sqadd
 * sqaddh
 * sqrt
 * sqrth
 * sra_n
 * sri_n (9 functions with unsupported types)
 * st1 (12 functions with unsupported types)
 * st2 (12 functions with unsupported types)
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
 * tst (6 functions with unsupported types)
 * uqadd
 * uqaddh
 * xar
 * zip (6 functions with unsupported types)
 * zip1 (7 functions with unsupported types)
 * zip2 (7 functions with unsupported types)
