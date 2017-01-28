#!/bin/bash
export LANG=C.UTF-8
find ~/camera/ -mtime +20 -type f -delete
exit 0;