#!/usr/bin/env python3
from setuptools import setup

from pathlib import Path
thisDir=Path(__file__).parent

formatsPath=thisDir / "kaitai_struct_formats"
kaitaiCfg={
	"formats":{
		"mifare_classic.py": {
			"path":"hardware/mifare/mifare_classic.ksy",
		}
	},
	"formatsRepo": {
		"git": "https://github.com/kaitai-io/kaitai_struct_formats.git",
		"localPath" : formatsPath,
		"update": True
	},
	"outputDir": thisDir / "MFCTool" ,
	"inputDir": formatsPath
}

setup(use_scm_version = True, kaitai=kaitaiCfg)
