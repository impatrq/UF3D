#pragma once
#define CONFIG_EXAMPLES_DIR "Custom/MakerPi_P3_PRO_SKR14"

/**
 * MakerPi P3 PRO on SKR V1.4 (LPC1768)
 * Single extruder, USB console, SD enabled.
 * Marlin bugfix-2.0.x baseline, minimal but safe.
 */

// ---------------- Machine identity ----------------
#define STRING_CONFIG_H_AUTHOR "(Lionel, MakerPi P3 PRO - SKR v1.4)"
#define CUSTOM_MACHINE_NAME "MakerPi P3 PRO"

// ---------------- Board & MCU ----------------
#define MOTHERBOARD BOARD_BTT_SKR_V1_4

// ---------------- Serial (USB only) ----------------
#define SERIAL_PORT -1
// #define SERIAL_PORT_2 0   // (unused) keep commented

// ---------------- Printer geometry ----------------
#define EXTRUDERS 1
#define DEFAULT_NOMINAL_FILAMENT_DIA 1.75

// Build volume (useful travel)
#define X_BED_SIZE 300
#define Y_BED_SIZE 300
#define Z_MAX_POS 180

// ---------------- Thermal settings ----------------
// Adjust if your thermistors are different
#define TEMP_SENSOR_0 1
#define TEMP_SENSOR_BED 1
#define HEATER_0_MAXTEMP 275
#define BED_MAXTEMP 120

// ---------------- Motion defaults (tune later) ----
#define DEFAULT_AXIS_STEPS_PER_UNIT   { 80, 80, 400, 93 }   // X, Y, Z, E
#define DEFAULT_MAX_FEEDRATE          { 300, 300, 5, 25 }
#define DEFAULT_MAX_ACCELERATION      { 3000, 3000, 100, 10000 }
#define DEFAULT_ACCELERATION          500
#define DEFAULT_TRAVEL_ACCELERATION   500

// ---------------- Bed leveling (OFF by default) ---
// Enable later if you add a probe (IR/BLTouch, etc.)
// #define AUTO_BED_LEVELING_BILINEAR
// #define Z_MIN_PROBE_USES_Z_MIN_ENDSTOP_PIN
// #define NOZZLE_TO_PROBE_OFFSET { 0, 0, -1.8 }
// #define RESTORE_LEVELING_AFTER_G28

// ---------------- SD / EEPROM ---------------------
#define SDSUPPORT
#define EEPROM_SETTINGS
// #define EEPROM_AUTO_INIT   // (optional) initialize automatically on first boot

// (rest of file unchanged)
