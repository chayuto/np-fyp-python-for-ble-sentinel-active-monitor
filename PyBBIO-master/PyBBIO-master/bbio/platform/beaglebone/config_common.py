# PyBBIO config file for bealebone

#---------------------------------------------------#
# Changes to this file may lead to permanent damage #
# to you Beaglebone, edit with care.                #
#---------------------------------------------------#

MMAP_OFFSET = 0x44c00000 
MMAP_SIZE   = 0x48ffffff-MMAP_OFFSET

##############################
##--- Start PRCM config: ---##
## Power Management and Clock Module

#--- Module clock control: ---
CM_PER = 0x44e00000-MMAP_OFFSET
CM_WKUP = 0x44e00400-MMAP_OFFSET

CM_PER_EPWMSS0_CLKCTRL = 0xd4+CM_PER
CM_PER_EPWMSS1_CLKCTRL = 0xcc+CM_PER
CM_PER_EPWMSS2_CLKCTRL = 0xd8+CM_PER

CM_WKUP_ADC_TSC_CLKCTRL = 0xbc+CM_WKUP

MODULEMODE_ENABLE = 0x02
IDLEST_MASK = 0x03<<16
# To enable module clock:
#  _setReg(CM_WKUP_module_CLKCTRL, MODULEMODE_ENABLE)
#  while (_getReg(CM_WKUP_module_CLKCTRL) & IDLEST_MASK): pass
# To disable module clock:
#  _andReg(CM_WKUP_module_CLKCTRL, ~MODULEMODE_ENABLE)
#-----------------------------

##--- End PRCM config ------##
##############################

########################################
##--- Start control module config: ---##

CONF_SLEW_SLOW    = 1<<6
CONF_RX_ACTIVE    = 1<<5
CONF_PULLUP       = 1<<4
CONF_PULLDOWN     = 0x00
CONF_PULL_DISABLE = 1<<3

CONF_GPIO_MODE   = 0x07 
CONF_GPIO_OUTPUT = CONF_GPIO_MODE
CONF_GPIO_INPUT  = CONF_GPIO_MODE | CONF_RX_ACTIVE
CONF_ADC_PIN     = CONF_RX_ACTIVE | CONF_PULL_DISABLE

##--- End control module config ------##
########################################

##############################
##--- Start GPIO config: ---##

GPIO0 = 0x44e07000-MMAP_OFFSET
GPIO1 = 0x4804c000-MMAP_OFFSET
GPIO2 = 0x481ac000-MMAP_OFFSET
GPIO3 = 0x481ae000-MMAP_OFFSET

GPIO_OE           = 0x134
GPIO_DATAIN       = 0x138
GPIO_DATAOUT      = 0x13c
GPIO_CLEARDATAOUT = 0x190
GPIO_SETDATAOUT   = 0x194

# Digital IO keywords:
INPUT    =  1
OUTPUT   =  0
PULLDOWN = -1
NOPULL   =  0
PULLUP   =  1
HIGH     =  1
LOW      =  0
RISING   =  1
FALLING  = -1
BOTH     =  0
MSBFIRST =  1
LSBFIRST = -1

## GPIO pins:

# GPIO pins must be in form: 
#             [GPIO_mux, bit_value, pinmux_filename, dt_offset], where 
# 'dt_offset' is the control module register offset from 44e10800, e.g.:
# "GPIO1_4" = [   GPIO1,      1<<4,      'gpmc_ad4',      0x10]  

GPIO = {
      "USR0" : [GPIO1, 1<<21,           'gpmc_a5', 0x054],
      "USR1" : [GPIO1, 1<<22,           'gpmc_a6', 0x058],
      "USR2" : [GPIO1, 1<<23,           'gpmc_a7', 0x05c],
      "USR3" : [GPIO1, 1<<24,           'gpmc_a8', 0x060],
   "GPIO0_2" : [GPIO0,  1<<2,         'spi0_sclk', 0x150],
   "GPIO0_3" : [GPIO0,  1<<3,           'spi0_d0', 0x154],
   "GPIO0_4" : [GPIO0,  1<<4,           'spi0_d1', 0x158],
   "GPIO0_5" : [GPIO0,  1<<5,          'spi0_cs0', 0x15c],
   "GPIO0_7" : [GPIO0,  1<<7, 'ecap0_in_pwm0_out', 0x164],
   "GPIO0_8" : [GPIO0,  1<<8,        'lcd_data12', 0x0d0],
   "GPIO0_9" : [GPIO0,  1<<9,        'lcd_data13', 0x0d4],
  "GPIO0_10" : [GPIO0, 1<<10,        'lcd_data14', 0x0d8],
  "GPIO0_11" : [GPIO0, 1<<11,        'lcd_data15', 0x0dc],
  "GPIO0_12" : [GPIO0, 1<<12,        'uart1_ctsn', 0x178],
  "GPIO0_13" : [GPIO0, 1<<13,        'uart1_rtsn', 0x17c],
  "GPIO0_14" : [GPIO0, 1<<14,         'uart1_rxd', 0x180],
  "GPIO0_15" : [GPIO0, 1<<15,         'uart1_txd', 0x184],
  "GPIO0_20" : [GPIO0, 1<<20,  'xdma_event_intr1', 0x1b4],
  "GPIO0_22" : [GPIO0, 1<<22,          'gpmc_ad8', 0x020],
  "GPIO0_23" : [GPIO0, 1<<23,          'gpmc_ad9', 0x024],
  "GPIO0_26" : [GPIO0, 1<<26,         'gpmc_ad10', 0x028],
  "GPIO0_27" : [GPIO0, 1<<27,         'gpmc_ad11', 0x02c],
  "GPIO0_30" : [GPIO0, 1<<30,        'gpmc_wait0', 0x070],
  "GPIO0_31" : [GPIO0, 1<<31,          'gpmc_wpn', 0x074],
   "GPIO1_0" : [GPIO1,     1,          'gpmc_ad0', 0x000],
   "GPIO1_1" : [GPIO1,  1<<1,          'gpmc_ad1', 0x004],
   "GPIO1_2" : [GPIO1,  1<<2,          'gpmc_ad2', 0x008],
   "GPIO1_3" : [GPIO1,  1<<3,          'gpmc_ad3', 0x00c],
   "GPIO1_4" : [GPIO1,  1<<4,          'gpmc_ad4', 0x010],
   "GPIO1_5" : [GPIO1,  1<<5,          'gpmc_ad5', 0x014],
   "GPIO1_6" : [GPIO1,  1<<6,          'gpmc_ad6', 0x018],
   "GPIO1_7" : [GPIO1,  1<<7,          'gpmc_ad7', 0x01c],
  "GPIO1_12" : [GPIO1, 1<<12,         'gpmc_ad12', 0x030],
  "GPIO1_13" : [GPIO1, 1<<13,         'gpmc_ad13', 0x034],
  "GPIO1_14" : [GPIO1, 1<<14,         'gpmc_ad14', 0x038],
  "GPIO1_15" : [GPIO1, 1<<15,         'gpmc_ad15', 0x03c],
  "GPIO1_16" : [GPIO1, 1<<16,           'gpmc_a0', 0x040],
  "GPIO1_17" : [GPIO1, 1<<17,           'gpmc_a1', 0x044],
  "GPIO1_18" : [GPIO1, 1<<18,           'gpmc_a2', 0x048],
  "GPIO1_19" : [GPIO1, 1<<19,           'gpmc_a3', 0x04c],
  "GPIO1_28" : [GPIO1, 1<<28,         'gpmc_ben1', 0x078],
  "GPIO1_29" : [GPIO1, 1<<29,         'gpmc_csn0', 0x07c],
  "GPIO1_30" : [GPIO1, 1<<30,         'gpmc_csn1', 0x080],
  "GPIO1_31" : [GPIO1, 1<<31,         'gpmc_csn2', 0x084],
   "GPIO2_1" : [GPIO2,  1<<1,          'gpmc_clk', 0x08c],
   "GPIO2_2" : [GPIO2,  1<<2,     'gpmc_advn_ale', 0x090],
   "GPIO2_3" : [GPIO2,  1<<3,      'gpmc_oen_ren', 0x094],
   "GPIO2_4" : [GPIO2,  1<<4,          'gpmc_wen', 0x098],
   "GPIO2_5" : [GPIO2,  1<<5,     'gpmc_ben0_cle', 0x09c],
   "GPIO2_6" : [GPIO2,  1<<6,         'lcd_data0', 0x0a0],
   "GPIO2_7" : [GPIO2,  1<<7,         'lcd_data1', 0x0a4],
   "GPIO2_8" : [GPIO2,  1<<8,         'lcd_data2', 0x0a8],
   "GPIO2_9" : [GPIO2,  1<<9,         'lcd_data3', 0x0ac],
  "GPIO2_10" : [GPIO2, 1<<10,         'lcd_data4', 0x0b0],
  "GPIO2_11" : [GPIO2, 1<<11,         'lcd_data5', 0x0b4],
  "GPIO2_12" : [GPIO2, 1<<12,         'lcd_data6', 0x0b8],
  "GPIO2_13" : [GPIO2, 1<<13,         'lcd_data7', 0x0bc],
  "GPIO2_14" : [GPIO2, 1<<14,         'lcd_data8', 0x0c0],
  "GPIO2_15" : [GPIO2, 1<<15,         'lcd_data9', 0x0c4],
  "GPIO2_16" : [GPIO2, 1<<16,        'lcd_data10', 0x0c8],
  "GPIO2_17" : [GPIO2, 1<<17,        'lcd_data11', 0x0cc],
  "GPIO2_22" : [GPIO2, 1<<22,         'lcd_vsync', 0x0e0],
  "GPIO2_23" : [GPIO2, 1<<23,         'lcd_hsync', 0x0e4],
  "GPIO2_24" : [GPIO2, 1<<24,          'lcd_pclk', 0x0e8],
  "GPIO2_25" : [GPIO2, 1<<25,    'lcd_ac_bias_en', 0x0ec],
  "GPIO3_14" : [GPIO3, 1<<14,      'mcasp0_aclkx', 0x190],
  "GPIO3_15" : [GPIO3, 1<<15,        'mcasp0_fsx', 0x194],
  "GPIO3_16" : [GPIO3, 1<<16,       'mcasp0_axr0', 0x198],
  "GPIO3_17" : [GPIO3, 1<<17,     'mcasp0_ahclkr', 0x19c],
  "GPIO3_19" : [GPIO3, 1<<19,        'mcasp0_fsr', 0x1a4],
  "GPIO3_21" : [GPIO3, 1<<21,     'mcasp0_ahclkx', 0x1ac]
}

# Having available pins in a dictionary makes it easy to
# check for invalid pins, but it's nice not to have to pass
# around strings, so here's some friendly constants:
USR0 = "USR0"
USR1 = "USR1"
USR2 = "USR2"
USR3 = "USR3"
GPIO0_2  = "GPIO0_2"
GPIO0_3  = "GPIO0_3"
GPIO0_4  = "GPIO0_4"
GPIO0_5  = "GPIO0_5"
GPIO0_7  = "GPIO0_7"
GPIO0_8  = "GPIO0_8"
GPIO0_9  = "GPIO0_9"
GPIO0_10 = "GPIO0_10"
GPIO0_11 = "GPIO0_11"
GPIO0_12 = "GPIO0_12"
GPIO0_13 = "GPIO0_13"
GPIO0_14 = "GPIO0_14"
GPIO0_15 = "GPIO0_15"
GPIO0_20 = "GPIO0_20"
GPIO0_22 = "GPIO0_22"
GPIO0_23 = "GPIO0_23"
GPIO0_26 = "GPIO0_26"
GPIO0_27 = "GPIO0_27"
GPIO0_30 = "GPIO0_30"
GPIO0_31 = "GPIO0_31"
GPIO1_0  = "GPIO1_0"
GPIO1_1  = "GPIO1_1"
GPIO1_2  = "GPIO1_2"
GPIO1_3  = "GPIO1_3"
GPIO1_4  = "GPIO1_4"
GPIO1_5  = "GPIO1_5"
GPIO1_6  = "GPIO1_6"
GPIO1_7  = "GPIO1_7"
GPIO1_12 = "GPIO1_12"
GPIO1_13 = "GPIO1_13"
GPIO1_14 = "GPIO1_14"
GPIO1_15 = "GPIO1_15"
GPIO1_16 = "GPIO1_16"
GPIO1_17 = "GPIO1_17"
GPIO1_18 = "GPIO1_18"
GPIO1_19 = "GPIO1_19"
GPIO1_28 = "GPIO1_28"
GPIO1_29 = "GPIO1_29"
GPIO1_30 = "GPIO1_30"
GPIO1_31 = "GPIO1_31"
GPIO2_1  = "GPIO2_1"
GPIO2_2  = "GPIO2_2"
GPIO2_3  = "GPIO2_3"
GPIO2_4  = "GPIO2_4"
GPIO2_5  = "GPIO2_5"
GPIO2_6  = "GPIO2_6"
GPIO2_7  = "GPIO2_7"
GPIO2_8  = "GPIO2_8"
GPIO2_9  = "GPIO2_9"
GPIO2_10 = "GPIO2_10"
GPIO2_11 = "GPIO2_11"
GPIO2_12 = "GPIO2_12"
GPIO2_13 = "GPIO2_13"
GPIO2_14 = "GPIO2_14"
GPIO2_15 = "GPIO2_15"
GPIO2_16 = "GPIO2_16"
GPIO2_17 = "GPIO2_17"
GPIO2_22 = "GPIO2_22"
GPIO2_23 = "GPIO2_23" 
GPIO2_24 = "GPIO2_24"
GPIO2_25 = "GPIO2_25"
GPIO3_14 = "GPIO3_14"
GPIO3_15 = "GPIO3_15"
GPIO3_16 = "GPIO3_16"
GPIO3_17 = "GPIO3_17"
GPIO3_19 = "GPIO3_19"
GPIO3_21 = "GPIO3_21"


##--- End GPIO config ------##
##############################


##############################
##--- Start UART config: ---##

# Formatting constants to mimic Arduino's serial.print() formatting:
DEC = 'DEC'
BIN = 'BIN'
OCT = 'OCT'
HEX = 'HEX'

##--- End UART config ------##
##############################


##############################
##--- Start PWM config: ----##

# Indexes in PWM_FILES lists:
PWM_REQUEST = 0
PWM_ENABLE  = 1
PWM_DUTY    = 2
PWM_FREQ    = 3

# Predefined resolutions for analogWrite():
RES_16BIT = 2**16
RES_8BIT  = 2**8
PERCENT   = 100

# Default frequency in Hz of PWM modules (must be >0):
PWM_DEFAULT_FREQ = 100000

##--- End PWM config: ------##
##############################
