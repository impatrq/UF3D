#pragma once
// No CONFIG_EXAMPLES_DIR here to avoid redefinition

/**
 * MakerPi P3 PRO on SKR V1.4 (LPC1768)
 * Advanced config: TMC2208 drivers, defaults otherwise.
 */

// ---------------- Stepper Drivers -----------------
#define X_DRIVER_TYPE  TMC2208
#define Y_DRIVER_TYPE  TMC2208
#define Z_DRIVER_TYPE  TMC2208
#define E0_DRIVER_TYPE TMC2208

// If your 2208s are in standalone (no UART wiring), this is fine.
// If later you wire UART, you can enable TMC features below.

// ---------------- TMC (optional UART features) ----
// #define TMC_USE_SW_SPI
// #define MONITOR_DRIVER_STATUS
// #define HYBRID_THRESHOLD
// #define STEALTHCHOP_XY
// #define STEALTHCHOP_Z
// #define STEALTHCHOP_E

// ---------------- SD / UI -------------------------
// Using USB + SD, no TFT for now. Keep defaults for LCD/TFT disabled.

// (rest of file unchanged)
