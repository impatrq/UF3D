/**
 * Marlin 3D Printer Firmware - Configuration_adv.h
 * Preset: MakerPi P3 PRO (Single Extruder) on BTT SKR v1.4, no LCD, no probe/ABL
 * Date: 2025-08-27
 *
 * Notes:
 * - Removed CONFIG_EXAMPLES_DIR to avoid redefinition warnings.
 * - ADVANCED_PAUSE_FEATURE DISABLED (no LCD / host-only). If you enable it, keep NOZZLE_PARK_FEATURE in Configuration.h.
 * - IDEX/DUAL_X_CARRIAGE disabled.
 * - TMC UART features not enabled (assuming TMC2208 standalone). If you use TMC2209/2208 UART, enable the relevant block.
 * - Keep defaults conservative to ensure compile on LPC1768.
 */

#pragma once

/**
 * DO NOT define CONFIG_EXAMPLES_DIR here to avoid redefinition with Configuration.h
 * // #define CONFIG_EXAMPLES_DIR "BIQU/B1 - SKR 1.4"
 */

//===========================================================================
//============================= Advanced Features ============================
//===========================================================================

// @section extras

// Emergency Parser: recommended for SKR v1.4
#define EMERGENCY_PARSER

// Host Keepalive: default
#define HOST_KEEPALIVE_FEATURE
#define DEFAULT_KEEPALIVE_INTERVAL 2

// ARC support (G2/G3) - keep off by default
// #define ARC_SUPPORT

// Gcode queue length
#define BLOCK_BUFFER_SIZE 16

//===========================================================================
//============================= Thermal Settings =============================
//===========================================================================

// Hotend protection tweaks are in Configuration.h. Leave defaults here.

// Hotend fan (auto) - OFF unless you wire a dedicated pin and set it in pins.
// #define E0_AUTO_FAN_PIN -1
// #define EXTRUDER_AUTO_FAN_TEMPERATURE 50
// #define EXTRUDER_AUTO_FAN_SPEED 255

//===========================================================================
//============================= Kinematics / Homing ==========================
//===========================================================================

// Allow Z after homing only (default on in many configs). Good safety w/o LCD.
#define PREVENT_COLD_EXTRUSION

// Homing bump: keep defaults
//#define HOMING_BUMP_MM { 5, 5, 2 }

//===========================================================================
//============================= Bed Leveling =================================
//===========================================================================

// No ABL / Probe in this preset. If you enable ABL in Configuration.h later,
// consider enabling related options here as needed (e.g., BABYSTEP_ZPROBE_OFFSET).

// Manual Mesh (optional; off by default here to keep simple build)
// #define MESH_BED_LEVELING
// #define MESH_INSET 10
// #define GRID_MAX_POINTS_X 5
// #define GRID_MAX_POINTS_Y 5
// #define MESH_EDIT_MENU   // needs LCD; leave off

//===========================================================================
//============================= Motion / Planner =============================
//===========================================================================

// Junction Deviation & S-curve are managed in Configuration.h. Keep planner defaults here.

//===========================================================================
//============================= Trinamic Drivers =============================
//===========================================================================

// Assuming TMC2208 in standalone mode. Leave UART features OFF.
// If you actually use UART (e.g., TMC2209 with DIAG), uncomment and configure.
//
// #define HAVE_TMC2208
// #define HAVE_TMC2209
// #define TMC_USE_SW_SPI
//
// Example UART config (ONLY if wired for UART):
// #define X_CURRENT       800  // mA
// #define X_MICROSTEPS    16
// #define X_RSENSE        0.110
// #define X_INTERPOLATE
// ... repeat for Y, Z, E0 ...

//===========================================================================
//============================= Additional Features ==========================
//===========================================================================

// SD Card
#define SDSUPPORT
#define LONG_FILENAME_HOST_SUPPORT

// Power-loss recovery enabled in Configuration.h; keep defaults here
//#define PLR_ENABLED_DEFAULT   true
//#define POWER_LOSS_PIN       -1

// No LCD tweaks here (no display installed)

// Filament Change / Advanced Pause
// Disabled to avoid NOZZLE_PARK dependency and LCD prompts for now.
/*
#define ADVANCED_PAUSE_FEATURE
#if ENABLED(ADVANCED_PAUSE_FEATURE)
  #define PAUSE_PARK_RETRACT_FEEDRATE  60  // (mm/s)
  #define PAUSE_PARK_RETRACT_LENGTH     2  // (mm)
  #define FILAMENT_CHANGE_UNLOAD_LENGTH 10 // (mm)
  #define FILAMENT_CHANGE_LOAD_LENGTH   10 // (mm)
#endif
*/

// No IDEX / Dual X Carriage
// #define DUAL_X_CARRIAGE

// Software endstops are handled by X/Y/Z_MIN/MAX_POS in Configuration.h

//===========================================================================
//============================= EEPROM / Storage =============================
//===========================================================================

// EEPROM is usually enabled/disabled in Configuration.h. Leave advanced tweaks default here.

//===========================================================================
//============================= Miscellaneous ================================
//===========================================================================

// Nozzle Park is defined in Configuration.h (needed only if Advanced Pause is on).
// Fan, RGB, Case light, Beeper, etc., omitted for minimal build in headless mode.

