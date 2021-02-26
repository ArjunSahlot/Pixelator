#!/bin/bash

download_link=https://github.com/ArjunSahlot/pixelator/archive/main.zip
temporary_dir=$(mktemp -d) \
&& curl -LO $download_link \
&& unzip -d $temporary_dir main.zip \
&& rm -rf main.zip \
&& mv $temporary_dir/pixelator-main $1/pixelator \
&& rm -rf $temporary_dir
echo -e "[0;32mSuccessfully downloaded to $1/pixelator[0m"
