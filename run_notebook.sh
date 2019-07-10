docker run -it \
            -p 8888:8888 \
            -v $(pwd)/notebook:/notebook \
            iagoeli/jupyter \
            '/bin/bash'
