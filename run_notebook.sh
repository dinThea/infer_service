docker run -it \
            -p 8888:8888 \
            -v $(pwd)/notebook:/notebook \
            iagoeli/opencv:4.1 \
            '/bin/bash'
