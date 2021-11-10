# ------------------------------------------------
# Generic Makefile (based on gcc)
#
#    target : GD32VF103
#    author : dataisland
# ------------------------------------------------

######################################
# target
######################################
TARGET = blink


######################################
# building variables
######################################
# debug build?
DEBUG = 1
# optimization
OPT = -Og


#######################################
# paths
#######################################
# Build path
BUILD_DIR = build
PACKAGE_DIR = ../../packages/GD32VF103
RISCV_PACKAGE = $(PACKAGE_DIR)/Firmware/RISCV/drivers

######################################
# source
######################################
# C sources
C_SOURCES = \
main.c \
$(RISCV_PACKAGE)/n200_func.c

# ASM sources
ASM_SOURCES  = \
startup_gd32vf103cb.s


#######################################
# binaries
#######################################
PREFIX = riscv32-unknown-elf-
ifdef GCC_PATH
CC = $(GCC_PATH)/$(PREFIX)gcc
AS = $(GCC_PATH)/$(PREFIX)gcc -x assembler-with-cpp
CP = $(GCC_PATH)/$(PREFIX)objcopy
SZ = $(GCC_PATH)/$(PREFIX)size
else
CC = $(PREFIX)gcc
AS = $(PREFIX)gcc -x assembler-with-cpp
CP = $(PREFIX)objcopy
SZ = $(PREFIX)size
endif
HEX = $(CP) -O ihex
BIN = $(CP) -O binary -S


#######################################
# CFLAGS
#######################################
# AS includes
AS_INCLUDES = \
-I$(RISCV_PACKAGE)

# C includes
C_INCLUDES =  \
-Iinclude \
-I$(RISCV_PACKAGE)

# common defines
COMMON_DEF = -march=rv32imac -mabi=ilp32 -mcmodel=medlow

# compile gcc flags
ASFLAGS = -c $(AS_INCLUDES) $(COMMON_DEF)
CFLAGS  = -c $(C_INCLUDES) $(COMMON_DEF) $(OPT) 

ifeq ($(DEBUG), 1)
CFLAGS += -g -gdwarf-2
endif


#######################################
# LDFLAGS
#######################################
# link script
LDSCRIPT = GD32VF103CB_FLASH.ld

# libraries
LIBS = -lc -lgcc
LDFLAGS = $(COMMON_DEF) $(LIBS) -T$(LDSCRIPT) -Wl,--no-relax -Wl,--gc-sections -nostdlib -nostartfiles --specs=nosys.specs

# default action: build all
all: $(BUILD_DIR)/$(TARGET).elf $(BUILD_DIR)/$(TARGET).hex $(BUILD_DIR)/$(TARGET).bin


#######################################
# build the application
#######################################
# list of objects
OBJECTS = $(addprefix $(BUILD_DIR)/,$(notdir $(C_SOURCES:.c=.o)))
vpath %.c $(sort $(dir $(C_SOURCES)))
# list of ASM program objects
OBJECTS += $(addprefix $(BUILD_DIR)/,$(notdir $(ASM_SOURCES:.s=.o)))
vpath %.s $(sort $(dir $(ASM_SOURCES)))

$(BUILD_DIR)/%.o: %.s Makefile | $(BUILD_DIR)
	$(AS) $(ASFLAGS) $< -o $@

$(BUILD_DIR)/%.o: %.c Makefile | $(BUILD_DIR) 
	$(CC) $(CFLAGS) $< -o $@

$(BUILD_DIR)/$(TARGET).elf: $(OBJECTS) Makefile
	$(CC) $(OBJECTS) $(LDFLAGS) -o $@
	$(SZ) $@

$(BUILD_DIR)/%.hex: $(BUILD_DIR)/%.elf | $(BUILD_DIR)
	$(HEX) $< $@

$(BUILD_DIR)/%.bin: $(BUILD_DIR)/%.elf | $(BUILD_DIR)
	$(BIN) $< $@

$(BUILD_DIR):
	mkdir $@

#######################################
# flash
#######################################
flash:
	sudo dfu-util -a 0 -s 0x8000000:leave -D $(BUILD_DIR)/$(TARGET).bin

#######################################
# clean up
#######################################
clean:
	rm -fR $(BUILD_DIR)
