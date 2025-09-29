/**
 * Marlin 3D Printer Firmware - Configuration.h (MakerPi P3 PRO - Single Extruder)
 * Update (sizes): Bed physical 310x310; printable 300x300; Z_MAX_POS 180.
 * Board: BTT SKR v1.4; No LCD; Single extruder.
 */
#pragma once

// --- Info --------------------------------------------------------------------
#define CONFIG_EXAMPLES_DIR "Custom/MakerPi_P3_PRO_Single"
#define CONFIGURATION_H_VERSION 02000905
#define STRING_CONFIG_H_AUTHOR "(ChatGPT, MakerPi P3 PRO single-extruder)"
#define SHOW_BOOTSCREEN

// --- Electronics / Board -----------------------------------------------------
#ifndef MOTHERBOARD
  #define MOTHERBOARD BOARD_BTT_SKR_V1_4
#endif

#define SERIAL_PORT 0
#define BAUDRATE 115200
#define SERIAL_PORT_2 -1

// --- Display -----------------------------------------------------------------
// No LCD/TFT connected for now.
//#define REPRAP_DISCOUNT_FULL_GRAPHIC_SMART_CONTROLLER
//#define DWIN_CREALITY_LCD

#define CUSTOM_MACHINE_NAME "MakerPi P3 PRO (Single)"

// --- Stepper Drivers ---------------------------------------------------------
#define X_DRIVER_TYPE  TMC2208
#define Y_DRIVER_TYPE  TMC2208
#define Z_DRIVER_TYPE  TMC2208
#define E0_DRIVER_TYPE TMC2208

// --- Extruders ---------------------------------------------------------------
#define EXTRUDERS 1

#define DEFAULT_NOMINAL_FILAMENT_DIA 1.75

// --- Thermal / Sensors -------------------------------------------------------
#define TEMP_SENSOR_0 1
#define TEMP_SENSOR_BED 1
#define TEMP_SENSOR_PROBE 0
#define TEMP_SENSOR_CHAMBER 0
#define TEMP_SENSOR_COOLER 0
#define TEMP_SENSOR_BOARD 0
#define TEMP_SENSOR_REDUNDANT 0

#define HEATER_0_MINTEMP   5
#define BED_MINTEMP        5

#define HEATER_0_MAXTEMP 275
#define BED_MAXTEMP      120

#define PIDTEMP
#define PIDTEMPBED
#define BANG_MAX 255
#define PID_MAX BANG_MAX
#define PID_K1 0.95

#if ENABLED(PIDTEMP)
  #define DEFAULT_Kp 22.20
  #define DEFAULT_Ki 1.08
  #define DEFAULT_Kd 114.00
#endif

#if ENABLED(PIDTEMPBED)
  #define DEFAULT_bedKp 120.00
  #define DEFAULT_bedKi 20.00
  #define DEFAULT_bedKd 250.00
#endif

#define PREVENT_COLD_EXTRUSION
#define EXTRUDE_MINTEMP 170
#define PREVENT_LENGTHY_EXTRUDE
#define EXTRUDE_MAXLENGTH 500

#define THERMAL_PROTECTION_HOTENDS
#define THERMAL_PROTECTION_BED

// --- Mechanics / Kinematics --------------------------------------------------
// Cartesian, single extruder.

// Endstops (assume MIN endstops; adjust if you use MAX)
#define USE_XMIN_PLUG
#define USE_YMIN_PLUG
#define USE_ZMIN_PLUG
#define ENDSTOPPULLUPS

// Inversion (verify with M119 on your wiring/sensors)
#define X_MIN_ENDSTOP_INVERTING true
#define Y_MIN_ENDSTOP_INVERTING true
#define Z_MIN_ENDSTOP_INVERTING true
#define X_MAX_ENDSTOP_INVERTING false
#define Y_MAX_ENDSTOP_INVERTING false
#define Z_MAX_ENDSTOP_INVERTING false
#define Z_MIN_PROBE_ENDSTOP_INVERTING false

// --- Motion defaults ---------------------------------------------------------
#define DEFAULT_AXIS_STEPS_PER_UNIT   { 80, 80, 400, 96 } // X, Y, Z, E0
#define DEFAULT_MAX_FEEDRATE          { 300, 300, 5, 25 }
#define DEFAULT_MAX_ACCELERATION      { 1000, 1000, 100, 5000 }

#define DEFAULT_ACCELERATION           500
#define DEFAULT_RETRACT_ACCELERATION   500
#define DEFAULT_TRAVEL_ACCELERATION    500

#define S_CURVE_ACCELERATION
#if DISABLED(CLASSIC_JERK)
  #define JUNCTION_DEVIATION_MM 0.08
#endif
#define DEFAULT_EJERK 5.0

// --- Geometry / Build Volume -------------------------------------------------
/**
 * Physical bed: 310 x 310 mm
 * Printable area: 300 x 300 mm
 * Z height: 180 mm
 */
#define X_BED_SIZE 300
#define Y_BED_SIZE 300
#define Z_MAX_POS  180

// --- Z Probe / Leveling ------------------------------------------------------
// If you have an IR probe (fixed), enable as needed.
//#define Z_MIN_PROBE_USES_Z_MIN_ENDSTOP_PIN
//#define FIX_MOUNTED_PROBE
//#define USE_PROBE_FOR_Z_HOMING

// Probe offsets (measure and update if using a probe)
#define NOZZLE_TO_PROBE_OFFSET { 24, -47, -1.5 }
#define PROBING_MARGIN 10
#define XY_PROBE_FEEDRATE (120*60)
#define Z_PROBE_FEEDRATE_FAST (4*60)
#define Z_PROBE_FEEDRATE_SLOW (Z_PROBE_FEEDRATE_FAST / 2)

// Mesh leveling (choose ONE; disable if not using ABL)
#define AUTO_BED_LEVELING_BILINEAR
#define RESTORE_LEVELING_AFTER_G28
#define GRID_MAX_POINTS_X 3
#define GRID_MAX_POINTS_Y 3
#define Z_SAFE_HOMING

// --- SD / Power loss ---------------------------------------------------------
#define SDSUPPORT
#define POWER_LOSS_RECOVERY

// --- Filament runout (optional) ---------------------------------------------
//#define FILAMENT_RUNOUT_SENSOR
#if ENABLED(FILAMENT_RUNOUT_SENSOR)
  #define FILAMENT_RUNOUT_DISTANCE_MM 5
  #define FILAMENT_RUNOUT_SCRIPT "M600"
#endif

// --- Misc --------------------------------------------------------------------
#define ENDSTOP_NOISE_THRESHOLD 4
#define PID_EDIT_MENU
#define PID_AUTOTUNE_MENU

// --- TODOs -------------------------------------------------------------------
/*
- Confirm endstop polarity with M119 and adjust *_ENDSTOP_INVERTING.
- Calibrate steps/mm (M92) and PID (M303) for your hardware.
- If you won't use a probe, you may disable AUTO_BED_LEVELING_* and offsets.
- If drivers are not TMC2208, set *_DRIVER_TYPE accordingly (e.g., TMC2209/A4988).
*/
