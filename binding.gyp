{
    "targets": [{
        "target_name": "node_soundio",
        "cflags!": [ "-fno-exceptions" ],
        "cflags_cc!": [ "-fno-exceptions" ],
        "sources": [
            "cppsrc/main.cpp",
            "cppsrc/shared/SoundIO.cpp",
            "cppsrc/device/AudioSpeakerDevice.cpp"
        ],
        'include_dirs': [
            "<!@(node -p \"require('node-addon-api').include\")",
            "lib",
            "cppsrc",
            "cppsrc/device",
            "cppsrc/input",
            "cppsrc/mixer",
            "cppsrc/output",
            "cppsrc/player",
            "cppsrc/shared",
            "cppsrc/utils"
        ],
        'libraries': [],
        'dependencies': [
            "<!(node -p \"require('node-addon-api').gyp\")"
        ],
        'defines': [ 'NAPI_DISABLE_CPP_EXCEPTIONS' ]
    }]
}