# name of your application
APPLICATION = riot-demo

# If no BOARD is found in the environment, use this default:
BOARD ?= nucleo-f411re

# This has to be the absolute path to the RIOT base directory:
RIOTBASE ?= $(CURDIR)/../../packages/RIOT

USEMODULE += ztimer_usec
USEMODULE += sched_round_robin

# Comment this out to disable code in RIOT that does safety checking
# which is not needed in a production environment but helps in the
# development process:
DEVELHELP ?= 1

# Change this to 0 show compiler invocation lines by default:
QUIET ?= 1

include $(RIOTBASE)/Makefile.include