/**
 * Marlin 3D Printer Firmware - Configuration.h (MakerPi P3 PRO - Single Extruder)
 * Fixed for compile errors:
 *  - Explicit X/Y/Z MIN/MAX
 *  - ABL disabled (no probe yet)
 *  - NOZZLE_PARK_FEATURE enabled (to satisfy ADVANCED_PAUSE sanity)
 */
#pragma once

#define CONFIG_EXAMPLES_DIR "Custom/MakerPi_P3_PRO_Single"
#define CONFIGURATION_H_VERSION 02000905
#define STRING_CONFIG_H_AUTHOR "(ChatGPT, MakerPi P3 PRO single-extruder)"
#define SHOW_BOOTSCREEN

#ifndef MOTHERBOARD
  #define MOTHERBOARD BOARD_BTT_SKR_V1_4
#endif

#define SERIAL_PORT 0
#define BAUDRATE 115200
#define SERIAL_PORT_2 -1

// No LCD for now
#define CUSTOM_MACHINE_NAME "MakerPi P3 PRO (Single)"

// Drivers
#define X_DRIVER_TYPE  TMC2208
#define Y_DRIVER_TYPE  TMC2208
#define Z_DRIVER_TYPE  TMC2208
#define E0_DRIVER_TYPE TMC2208

// Extruders
#define EXTRUDERS 1
#define DEFAULT_NOMINAL_FILAMENT_DIA 1.75

// Thermal
#define TEMP_SENSOR_0 1
#define TEMP_SENSOR_BED 1
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

// Endstops
#define USE_XMIN_PLUG
#define USE_YMIN_PLUG
#define USE_ZMIN_PLUG
#define ENDSTOPPULLUPS
#define X_MIN_ENDSTOP_INVERTING true
#define Y_MIN_ENDSTOP_INVERTING true
#define Z_MIN_ENDSTOP_INVERTING true
#define X_MAX_ENDSTOP_INVERTING false
#define Y_MAX_ENDSTOP_INVERTING false
#define Z_MAX_ENDSTOP_INVERTING false
#define Z_MIN_PROBE_ENDSTOP_INVERTING false

// Motion
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

// Geometry / Build Volume
// Physical bed: 310x310; Printable: 300x300; Z: 180
#define X_BED_SIZE 300
#define Y_BED_SIZE 300
#define Z_MAX_POS  180

// Explicit software endstops to satisfy sanity checks
#define X_MIN_POS 0
#define Y_MIN_POS 0
#define Z_MIN_POS 0
#define X_MAX_POS X_BED_SIZE
#define Y_MAX_POS Y_BED_SIZE
// Z_MAX_POS already defined above

// Probing / Leveling
// -- No probe now: disable ABL --
#undef AUTO_BED_LEVELING_BILINEAR
//#define AUTO_BED_LEVELING_BILINEAR  // leave disabled
//#define Z_MIN_PROBE_USES_Z_MIN_ENDSTOP_PIN
//#define FIX_MOUNTED_PROBE
//#define USE_PROBE_FOR_Z_HOMING
//#define MESH_BED_LEVELING          // Optional: enable if you want manual mesh (requires a way to move Z)
#undef Z_SAFE_HOMING

// SD / Power loss
#define SDSUPPORT
#define POWER_LOSS_RECOVERY

// Filament runout (optional)
//#define FILAMENT_RUNOUT_SENSOR
#if ENABLED(FILAMENT_RUNOUT_SENSOR)
  #define FILAMENT_RUNOUT_DISTANCE_MM 5
  #define FILAMENT_RUNOUT_SCRIPT "M600"
#endif

// Quality of life
#define ENDSTOP_NOISE_THRESHOLD 4
#define PID_EDIT_MENU
#define PID_AUTOTUNE_MENU

// Parking (needed if ADVANCED_PAUSE_FEATURE is enabled in adv)
#define NOZZLE_PARK_FEATURE
#define NOZZLE_PARK_POINT { (X_BED_SIZE - 5), (Y_BED_SIZE - 5), 20 } // safe park at far corner
