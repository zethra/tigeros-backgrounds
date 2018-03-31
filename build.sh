#!/bin/bash

tar -cvf tigeros-backgrounds.tar.gz tigeros-backgrounds-1.0/
fedpkg --release f27 local
