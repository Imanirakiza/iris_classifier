{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "c79e372e",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Collecting streamlit\n",
      "  Downloading streamlit-1.17.0-py2.py3-none-any.whl (9.3 MB)\n",
      "Collecting altair>=3.2.0\n",
      "  Downloading altair-4.2.2-py3-none-any.whl (813 kB)\n",
      "Collecting validators>=0.2\n",
      "  Downloading validators-0.20.0.tar.gz (30 kB)\n",
      "Collecting rich>=10.11.0\n",
      "  Downloading rich-13.3.1-py3-none-any.whl (239 kB)\n",
      "Collecting toml\n",
      "  Downloading toml-0.10.2-py2.py3-none-any.whl (16 kB)\n",
      "Collecting pympler>=0.9\n",
      "  Downloading Pympler-1.0.1-py3-none-any.whl (164 kB)\n",
      "Collecting pydeck>=0.1.dev5\n",
      "  Downloading pydeck-0.8.0-py2.py3-none-any.whl (4.7 MB)\n",
      "Collecting requests>=2.4\n",
      "  Downloading requests-2.28.2-py3-none-any.whl (62 kB)\n",
      "Collecting importlib-metadata>=1.4\n",
      "  Downloading importlib_metadata-6.0.0-py3-none-any.whl (21 kB)\n",
      "Collecting blinker>=1.0.0\n",
      "  Downloading blinker-1.5-py2.py3-none-any.whl (12 kB)\n",
      "Collecting cachetools>=4.0\n",
      "  Downloading cachetools-5.3.0-py3-none-any.whl (9.3 kB)\n",
      "Requirement already satisfied: pillow>=6.2.0 in c:\\users\\dell\\anaconda3\\envs\\env1\\lib\\site-packages (from streamlit) (9.0.1)\n",
      "Collecting tzlocal>=1.1\n",
      "  Downloading tzlocal-4.2-py3-none-any.whl (19 kB)\n",
      "Collecting semver\n",
      "  Downloading semver-2.13.0-py2.py3-none-any.whl (12 kB)\n",
      "Requirement already satisfied: typing-extensions>=3.10.0.0 in c:\\users\\dell\\anaconda3\\envs\\env1\\lib\\site-packages (from streamlit) (4.1.1)\n",
      "Requirement already satisfied: tornado>=5.0 in c:\\users\\dell\\anaconda3\\envs\\env1\\lib\\site-packages (from streamlit) (6.1)\n",
      "Collecting gitpython!=3.1.19\n",
      "  Downloading GitPython-3.1.30-py3-none-any.whl (184 kB)\n",
      "Requirement already satisfied: python-dateutil in c:\\users\\dell\\anaconda3\\envs\\env1\\lib\\site-packages (from streamlit) (2.8.2)\n",
      "Collecting pyarrow>=4.0\n",
      "  Downloading pyarrow-11.0.0-cp38-cp38-win_amd64.whl (20.6 MB)\n",
      "Requirement already satisfied: numpy in c:\\users\\dell\\anaconda3\\envs\\env1\\lib\\site-packages (from streamlit) (1.22.3)\n",
      "Collecting watchdog\n",
      "  Downloading watchdog-2.2.1-py3-none-win_amd64.whl (78 kB)\n",
      "Collecting protobuf<4,>=3.12\n",
      "  Downloading protobuf-3.20.3-cp38-cp38-win_amd64.whl (904 kB)\n",
      "Collecting click>=7.0\n",
      "  Downloading click-8.1.3-py3-none-any.whl (96 kB)\n",
      "Requirement already satisfied: pandas>=0.21.0 in c:\\users\\dell\\anaconda3\\envs\\env1\\lib\\site-packages (from streamlit) (1.5.2)\n",
      "Requirement already satisfied: packaging>=14.1 in c:\\users\\dell\\anaconda3\\envs\\env1\\lib\\site-packages (from streamlit) (21.3)\n",
      "Collecting toolz\n",
      "  Downloading toolz-0.12.0-py3-none-any.whl (55 kB)\n",
      "Requirement already satisfied: entrypoints in c:\\users\\dell\\anaconda3\\envs\\env1\\lib\\site-packages (from altair>=3.2.0->streamlit) (0.4)\n",
      "Requirement already satisfied: jinja2 in c:\\users\\dell\\anaconda3\\envs\\env1\\lib\\site-packages (from altair>=3.2.0->streamlit) (3.0.3)\n",
      "Requirement already satisfied: jsonschema>=3.0 in c:\\users\\dell\\anaconda3\\envs\\env1\\lib\\site-packages (from altair>=3.2.0->streamlit) (4.4.0)\n",
      "Requirement already satisfied: colorama in c:\\users\\dell\\anaconda3\\envs\\env1\\lib\\site-packages (from click>=7.0->streamlit) (0.4.4)\n",
      "Collecting gitdb<5,>=4.0.1\n",
      "  Downloading gitdb-4.0.10-py3-none-any.whl (62 kB)\n",
      "Collecting smmap<6,>=3.0.1\n",
      "  Downloading smmap-5.0.0-py3-none-any.whl (24 kB)\n",
      "Requirement already satisfied: zipp>=0.5 in c:\\users\\dell\\anaconda3\\envs\\env1\\lib\\site-packages (from importlib-metadata>=1.4->streamlit) (3.8.0)\n",
      "Requirement already satisfied: pyrsistent!=0.17.0,!=0.17.1,!=0.17.2,>=0.14.0 in c:\\users\\dell\\anaconda3\\envs\\env1\\lib\\site-packages (from jsonschema>=3.0->altair>=3.2.0->streamlit) (0.18.0)\n",
      "Requirement already satisfied: attrs>=17.4.0 in c:\\users\\dell\\anaconda3\\envs\\env1\\lib\\site-packages (from jsonschema>=3.0->altair>=3.2.0->streamlit) (21.4.0)\n",
      "Requirement already satisfied: importlib-resources>=1.4.0 in c:\\users\\dell\\anaconda3\\envs\\env1\\lib\\site-packages (from jsonschema>=3.0->altair>=3.2.0->streamlit) (5.2.0)\n",
      "Requirement already satisfied: pyparsing!=3.0.5,>=2.0.2 in c:\\users\\dell\\anaconda3\\envs\\env1\\lib\\site-packages (from packaging>=14.1->streamlit) (3.0.4)\n",
      "Requirement already satisfied: pytz>=2020.1 in c:\\users\\dell\\anaconda3\\envs\\env1\\lib\\site-packages (from pandas>=0.21.0->streamlit) (2022.7)\n",
      "Requirement already satisfied: MarkupSafe>=2.0 in c:\\users\\dell\\anaconda3\\envs\\env1\\lib\\site-packages (from jinja2->altair>=3.2.0->streamlit) (2.0.1)\n",
      "Requirement already satisfied: six>=1.5 in c:\\users\\dell\\anaconda3\\envs\\env1\\lib\\site-packages (from python-dateutil->streamlit) (1.16.0)\n",
      "Collecting idna<4,>=2.5\n",
      "  Downloading idna-3.4-py3-none-any.whl (61 kB)\n",
      "Requirement already satisfied: certifi>=2017.4.17 in c:\\users\\dell\\anaconda3\\envs\\env1\\lib\\site-packages (from requests>=2.4->streamlit) (2022.12.7)\n",
      "Collecting charset-normalizer<4,>=2\n",
      "  Downloading charset_normalizer-3.0.1-cp38-cp38-win_amd64.whl (95 kB)\n",
      "Collecting urllib3<1.27,>=1.21.1\n",
      "  Downloading urllib3-1.26.14-py2.py3-none-any.whl (140 kB)\n",
      "Note: you may need to restart the kernel to use updated packages.\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "ERROR: pip's dependency resolver does not currently take into account all the packages that are installed. This behaviour is the source of the following dependency conflicts.\n",
      "tensorflow 2.5.0 requires absl-py~=0.10, which is not installed.\n",
      "tensorflow 2.5.0 requires astunparse~=1.6.3, which is not installed.\n",
      "tensorflow 2.5.0 requires gast==0.4.0, which is not installed.\n",
      "tensorflow 2.5.0 requires google-pasta~=0.2, which is not installed.\n",
      "tensorflow 2.5.0 requires keras-preprocessing~=1.1.2, which is not installed.\n",
      "tensorflow 2.5.0 requires opt-einsum~=3.3.0, which is not installed.\n",
      "tensorflow 2.5.0 requires tensorflow-estimator<2.6.0,>=2.5.0rc0, which is not installed.\n",
      "tensorflow 2.5.0 requires termcolor~=1.1.0, which is not installed.\n",
      "tensorflow 2.5.0 requires wrapt~=1.12.1, which is not installed.\n",
      "tensorboard 2.5.0 requires absl-py>=0.4, which is not installed.\n",
      "tensorboard 2.5.0 requires google-auth<2,>=1.6.3, which is not installed.\n",
      "tensorboard 2.5.0 requires google-auth-oauthlib<0.5,>=0.4.1, which is not installed.\n",
      "tensorboard 2.5.0 requires markdown>=2.6.8, which is not installed.\n",
      "tensorboard 2.5.0 requires tensorboard-data-server<0.7.0,>=0.6.0, which is not installed.\n",
      "tensorboard 2.5.0 requires tensorboard-plugin-wit>=1.6.0, which is not installed.\n",
      "tensorboard 2.5.0 requires werkzeug>=0.11.15, which is not installed.\n",
      "tensorflow 2.5.0 requires numpy~=1.19.2, but you have numpy 1.22.3 which is incompatible.\n",
      "tensorflow 2.5.0 requires six~=1.15.0, but you have six 1.16.0 which is incompatible.\n",
      "tensorflow 2.5.0 requires typing-extensions~=3.7.4, but you have typing-extensions 4.1.1 which is incompatible.\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Collecting pygments<3.0.0,>=2.14.0\n",
      "  Downloading Pygments-2.14.0-py3-none-any.whl (1.1 MB)\n",
      "Collecting markdown-it-py<3.0.0,>=2.1.0\n",
      "  Downloading markdown_it_py-2.1.0-py3-none-any.whl (84 kB)\n",
      "Collecting mdurl~=0.1\n",
      "  Downloading mdurl-0.1.2-py3-none-any.whl (10.0 kB)\n",
      "Collecting pytz-deprecation-shim\n",
      "  Downloading pytz_deprecation_shim-0.1.0.post0-py2.py3-none-any.whl (15 kB)\n",
      "Collecting backports.zoneinfo\n",
      "  Downloading backports.zoneinfo-0.2.1-cp38-cp38-win_amd64.whl (38 kB)\n",
      "Collecting tzdata\n",
      "  Downloading tzdata-2022.7-py2.py3-none-any.whl (340 kB)\n",
      "Requirement already satisfied: decorator>=3.4.0 in c:\\users\\dell\\anaconda3\\envs\\env1\\lib\\site-packages (from validators>=0.2->streamlit) (5.1.1)\n",
      "Building wheels for collected packages: validators\n",
      "  Building wheel for validators (setup.py): started\n",
      "  Building wheel for validators (setup.py): finished with status 'done'\n",
      "  Created wheel for validators: filename=validators-0.20.0-py3-none-any.whl size=19582 sha256=a8063f227efc8fee24a632de62c33d66aa1115cfca58ee32182f2f09a0a228df\n",
      "  Stored in directory: c:\\users\\dell\\appdata\\local\\pip\\cache\\wheels\\19\\09\\72\\3eb74d236bb48bd0f3c6c3c83e4e0c5bbfcbcad7c6c3539db8\n",
      "Successfully built validators\n",
      "Installing collected packages: tzdata, smmap, mdurl, backports.zoneinfo, urllib3, toolz, pytz-deprecation-shim, pygments, markdown-it-py, idna, gitdb, charset-normalizer, watchdog, validators, tzlocal, toml, semver, rich, requests, pympler, pydeck, pyarrow, protobuf, importlib-metadata, gitpython, click, cachetools, blinker, altair, streamlit\n",
      "  Attempting uninstall: pygments\n",
      "    Found existing installation: Pygments 2.11.2\n",
      "    Uninstalling Pygments-2.11.2:\n",
      "      Successfully uninstalled Pygments-2.11.2\n",
      "Successfully installed altair-4.2.2 backports.zoneinfo-0.2.1 blinker-1.5 cachetools-5.3.0 charset-normalizer-3.0.1 click-8.1.3 gitdb-4.0.10 gitpython-3.1.30 idna-3.4 importlib-metadata-6.0.0 markdown-it-py-2.1.0 mdurl-0.1.2 protobuf-3.20.3 pyarrow-11.0.0 pydeck-0.8.0 pygments-2.14.0 pympler-1.0.1 pytz-deprecation-shim-0.1.0.post0 requests-2.28.2 rich-13.3.1 semver-2.13.0 smmap-5.0.0 streamlit-1.17.0 toml-0.10.2 toolz-0.12.0 tzdata-2022.7 tzlocal-4.2 urllib3-1.26.14 validators-0.20.0 watchdog-2.2.1\n"
     ]
    }
   ],
   "source": [
    "pip install streamlit "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "7d742b29",
   "metadata": {},
   "outputs": [],
   "source": [
    "import streamlit as st\n",
    "import pandas as pd\n",
    "import numpy as np\n",
    "# from prediction import predict"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "8dc81313",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "2023-02-09 20:39:44.404 \n",
      "  \u001b[33m\u001b[1mWarning:\u001b[0m to view this Streamlit app on a browser, run it with the following\n",
      "  command:\n",
      "\n",
      "    streamlit run C:\\Users\\Dell\\anaconda3\\envs\\env1\\lib\\site-packages\\ipykernel_launcher.py [ARGUMENTS]\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "DeltaGenerator(_root_container=0, _provided_cursor=None, _parent=None, _block_type=None, _form_data=None)"
      ]
     },
     "execution_count": 6,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "st.title('Classifying Iris Flowers')\n",
    "st.markdown('Toy model to play to classify iris flowers into \\\n",
    "setosa, versicolor, virginica')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "d87ad7b2",
   "metadata": {},
   "outputs": [],
   "source": [
    "st.header('Plant Features')\n",
    "col1, col2 = st.columns(2)\n",
    "with col1:\n",
    "    st.text('Sepal characteristics')\n",
    "    sepal_l = st.slider('Sepal lenght (cm)', 1.0, 8.0, 0.5)\n",
    "    sepal_w = st.slider('Sepal width (cm)', 2.0, 4.4, 0.5)\n",
    "with col2:\n",
    "    st.text('Pepal characteristics')\n",
    "    petal_l = st.slider('Petal lenght (cm)', 1.0, 7.0, 0.5)\n",
    "    petal_w = st.slider('Petal width (cm)', 0.1, 2.5, 0.5)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "id": "9bc1d6d9",
   "metadata": {},
   "outputs": [],
   "source": [
    "if st.button(\"Predict type of Iris\"):\n",
    "    result = predict(np.array([[sepal_l, sepal_w, petal_l, petal_w]]))\n",
    "    st.text(result[0])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "id": "e89ce43b",
   "metadata": {},
   "outputs": [],
   "source": [
    "# streamlit run app.py"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "da5bd50d",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.13"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
