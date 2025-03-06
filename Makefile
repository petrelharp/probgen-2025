SHELL := /bin/bash
# use bash for <( ) syntax

.PHONY : setup

TARGET := probgen-2025.slides.html

$(TARGET) : setup

setup :
	$(MAKE) -C figs

publish : $(TARGET)
	# do this after giving the talk
	sed -i '/mathjax: .*MathJax.js/d' $<

include rules.mk
