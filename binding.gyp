{
	"targets": [{
		"target_name": "napi_test",
		"include_dirs": [
			"src",
      "<!(node -p \"require('node-addon-api').include_dir\")"
		],
		"sources": [
			"src/test.h",
			"src/test.cc"
		],
    'defines': [ 'NAPI_DISABLE_CPP_EXCEPTIONS' ],
    'cflags!': [ '-fno-exceptions' ],
    'cflags_cc!': [ '-fno-exceptions' ],
		"conditions": [
			["OS!='mac'", {
        'cflags+': ['-fvisibility=hidden'],
        'xcode_settings': {
          'GCC_ENABLE_CPP_EXCEPTIONS': 'YES',
          'CLANG_CXX_LIBRARY': 'libc++',
          'MACOSX_DEPLOYMENT_TARGET': '10.7',
          'GCC_SYMBOLS_PRIVATE_EXTERN': 'YES', # -fvisibility=hidden
        },
				"libraries": [
					"-lrt"
				]
			}]
		],
	}]
}
