# FROM mltooling/ml-workspace-spark:0.8.7
FROM mltooling/ml-workspace:0.13.2
ENV RESOURCES_PATH="/resources" \
    CONDA_PYTHON_DIR=/opt/conda/lib/python3.8

COPY resources/branding $RESOURCES_PATH/branding

RUN cp -f $RESOURCES_PATH/branding/logo.png $CONDA_PYTHON_DIR"/site-packages/notebook/static/base/images/logo.png" && \
    cp -f $RESOURCES_PATH/branding/favicon.ico $CONDA_PYTHON_DIR"/site-packages/notebook/static/base/images/favicon.ico" && \
    cp -f $RESOURCES_PATH/branding/favicon.ico $CONDA_PYTHON_DIR"/site-packages/notebook/static/favicon.ico" && \
    cp -f $RESOURCES_PATH/branding/favicon.ico $RESOURCES_PATH"/filebrowser/img/icons/favicon.ico" && \
    cp -f $RESOURCES_PATH/branding/favicon.ico $RESOURCES_PATH"/filebrowser/img/icons/favicon-32x32.png" && \
    cp -f $RESOURCES_PATH/branding/favicon.ico $RESOURCES_PATH"/filebrowser/img/icons/favicon-16x16.png" && \
    cp -f $RESOURCES_PATH/branding/ml-workspace-logo.svg $RESOURCES_PATH"/filebrowser/img/logo.svg" && \
    jupyter nbextension disable varInspector/main && \
    jupyter nbextension disable spellchecker/main && \
    jupyter nbextension enable scratchpad/main && \
    jupyter nbextension enable init_cell/main && \
    jupyter nbextension enable code_prettify/code_prettify
