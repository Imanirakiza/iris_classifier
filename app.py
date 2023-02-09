{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "c79e372e",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Requirement already satisfied: streamlit in c:\\users\\dell\\anaconda3\\envs\\env1\\lib\\site-packages (1.17.0)Note: you may need to restart the kernel to use updated packages.\n",
      "Requirement already satisfied: validators>=0.2 in c:\\users\\dell\\anaconda3\\envs\\env1\\lib\\site-packages (from streamlit) (0.20.0)\n",
      "Requirement already satisfied: importlib-metadata>=1.4 in c:\\users\\dell\\anaconda3\\envs\\env1\\lib\\site-packages (from streamlit) (6.0.0)\n",
      "Requirement already satisfied: blinker>=1.0.0 in c:\\users\\dell\\anaconda3\\envs\\env1\\lib\\site-packages (from streamlit) (1.5)\n",
      "Requirement already satisfied: cachetools>=4.0 in c:\\users\\dell\\anaconda3\\envs\\env1\\lib\\site-packages (from streamlit) (5.3.0)\n",
      "Requirement already satisfied: pydeck>=0.1.dev5 in c:\\users\\dell\\anaconda3\\envs\\env1\\lib\\site-packages (from streamlit) (0.8.0)\n",
      "Requirement already satisfied: protobuf<4,>=3.12 in c:\\users\\dell\\anaconda3\\envs\\env1\\lib\\site-packages (from streamlit) (3.20.3)\n",
      "Requirement already satisfied: numpy in c:\\users\\dell\\anaconda3\\envs\\env1\\lib\\site-packages (from streamlit) (1.22.3)\n",
      "Requirement already satisfied: pillow>=6.2.0 in c:\\users\\dell\\anaconda3\\envs\\env1\\lib\\site-packages (from streamlit) (9.0.1)\n",
      "Requirement already satisfied: tzlocal>=1.1 in c:\\users\\dell\\anaconda3\\envs\\env1\\lib\\site-packages (from streamlit) (4.2)\n",
      "Requirement already satisfied: semver in c:\\users\\dell\\anaconda3\\envs\\env1\\lib\\site-packages (from streamlit) (2.13.0)\n",
      "Requirement already satisfied: python-dateutil in c:\\users\\dell\\anaconda3\\envs\\env1\\lib\\site-packages (from streamlit) (2.8.2)\n",
      "Requirement already satisfied: toml in c:\\users\\dell\\anaconda3\\envs\\env1\\lib\\site-packages (from streamlit) (0.10.2)\n",
      "Requirement already satisfied: pyarrow>=4.0 in c:\\users\\dell\\anaconda3\\envs\\env1\\lib\\site-packages (from streamlit) (11.0.0)\n",
      "Requirement already satisfied: tornado>=5.0 in c:\\users\\dell\\anaconda3\\envs\\env1\\lib\\site-packages (from streamlit) (6.1)\n",
      "\n",
      "Requirement already satisfied: requests>=2.4 in c:\\users\\dell\\anaconda3\\envs\\env1\\lib\\site-packages (from streamlit) (2.28.2)\n",
      "Requirement already satisfied: pympler>=0.9 in c:\\users\\dell\\anaconda3\\envs\\env1\\lib\\site-packages (from streamlit) (1.0.1)\n",
      "Requirement already satisfied: gitpython!=3.1.19 in c:\\users\\dell\\anaconda3\\envs\\env1\\lib\\site-packages (from streamlit) (3.1.30)\n",
      "Requirement already satisfied: typing-extensions>=3.10.0.0 in c:\\users\\dell\\anaconda3\\envs\\env1\\lib\\site-packages (from streamlit) (4.1.1)\n",
      "Requirement already satisfied: watchdog in c:\\users\\dell\\anaconda3\\envs\\env1\\lib\\site-packages (from streamlit) (2.2.1)\n",
      "Requirement already satisfied: click>=7.0 in c:\\users\\dell\\anaconda3\\envs\\env1\\lib\\site-packages (from streamlit) (8.1.3)\n",
      "Requirement already satisfied: pandas>=0.21.0 in c:\\users\\dell\\anaconda3\\envs\\env1\\lib\\site-packages (from streamlit) (1.5.2)\n",
      "Requirement already satisfied: packaging>=14.1 in c:\\users\\dell\\anaconda3\\envs\\env1\\lib\\site-packages (from streamlit) (21.3)\n",
      "Requirement already satisfied: rich>=10.11.0 in c:\\users\\dell\\anaconda3\\envs\\env1\\lib\\site-packages (from streamlit) (13.3.1)\n",
      "Requirement already satisfied: altair>=3.2.0 in c:\\users\\dell\\anaconda3\\envs\\env1\\lib\\site-packages (from streamlit) (4.2.2)\n",
      "Requirement already satisfied: toolz in c:\\users\\dell\\anaconda3\\envs\\env1\\lib\\site-packages (from altair>=3.2.0->streamlit) (0.12.0)\n",
      "Requirement already satisfied: jinja2 in c:\\users\\dell\\anaconda3\\envs\\env1\\lib\\site-packages (from altair>=3.2.0->streamlit) (3.0.3)\n",
      "Requirement already satisfied: entrypoints in c:\\users\\dell\\anaconda3\\envs\\env1\\lib\\site-packages (from altair>=3.2.0->streamlit) (0.4)\n",
      "Requirement already satisfied: jsonschema>=3.0 in c:\\users\\dell\\anaconda3\\envs\\env1\\lib\\site-packages (from altair>=3.2.0->streamlit) (4.4.0)\n",
      "Requirement already satisfied: colorama in c:\\users\\dell\\anaconda3\\envs\\env1\\lib\\site-packages (from click>=7.0->streamlit) (0.4.4)\n",
      "Requirement already satisfied: gitdb<5,>=4.0.1 in c:\\users\\dell\\anaconda3\\envs\\env1\\lib\\site-packages (from gitpython!=3.1.19->streamlit) (4.0.10)\n",
      "Requirement already satisfied: smmap<6,>=3.0.1 in c:\\users\\dell\\anaconda3\\envs\\env1\\lib\\site-packages (from gitdb<5,>=4.0.1->gitpython!=3.1.19->streamlit) (5.0.0)\n",
      "Requirement already satisfied: zipp>=0.5 in c:\\users\\dell\\anaconda3\\envs\\env1\\lib\\site-packages (from importlib-metadata>=1.4->streamlit) (3.8.0)\n",
      "Requirement already satisfied: pyrsistent!=0.17.0,!=0.17.1,!=0.17.2,>=0.14.0 in c:\\users\\dell\\anaconda3\\envs\\env1\\lib\\site-packages (from jsonschema>=3.0->altair>=3.2.0->streamlit) (0.18.0)\n",
      "Requirement already satisfied: importlib-resources>=1.4.0 in c:\\users\\dell\\anaconda3\\envs\\env1\\lib\\site-packages (from jsonschema>=3.0->altair>=3.2.0->streamlit) (5.2.0)\n",
      "Requirement already satisfied: attrs>=17.4.0 in c:\\users\\dell\\anaconda3\\envs\\env1\\lib\\site-packages (from jsonschema>=3.0->altair>=3.2.0->streamlit) (21.4.0)\n",
      "Requirement already satisfied: pyparsing!=3.0.5,>=2.0.2 in c:\\users\\dell\\anaconda3\\envs\\env1\\lib\\site-packages (from packaging>=14.1->streamlit) (3.0.4)\n",
      "Requirement already satisfied: pytz>=2020.1 in c:\\users\\dell\\anaconda3\\envs\\env1\\lib\\site-packages (from pandas>=0.21.0->streamlit) (2022.7)\n",
      "Requirement already satisfied: MarkupSafe>=2.0 in c:\\users\\dell\\anaconda3\\envs\\env1\\lib\\site-packages (from jinja2->altair>=3.2.0->streamlit) (2.0.1)\n",
      "Requirement already satisfied: six>=1.5 in c:\\users\\dell\\anaconda3\\envs\\env1\\lib\\site-packages (from python-dateutil->streamlit) (1.16.0)\n",
      "Requirement already satisfied: urllib3<1.27,>=1.21.1 in c:\\users\\dell\\anaconda3\\envs\\env1\\lib\\site-packages (from requests>=2.4->streamlit) (1.26.14)\n",
      "Requirement already satisfied: certifi>=2017.4.17 in c:\\users\\dell\\anaconda3\\envs\\env1\\lib\\site-packages (from requests>=2.4->streamlit) (2022.12.7)\n",
      "Requirement already satisfied: charset-normalizer<4,>=2 in c:\\users\\dell\\anaconda3\\envs\\env1\\lib\\site-packages (from requests>=2.4->streamlit) (3.0.1)\n",
      "Requirement already satisfied: idna<4,>=2.5 in c:\\users\\dell\\anaconda3\\envs\\env1\\lib\\site-packages (from requests>=2.4->streamlit) (3.4)\n",
      "Requirement already satisfied: pygments<3.0.0,>=2.14.0 in c:\\users\\dell\\anaconda3\\envs\\env1\\lib\\site-packages (from rich>=10.11.0->streamlit) (2.14.0)\n",
      "Requirement already satisfied: markdown-it-py<3.0.0,>=2.1.0 in c:\\users\\dell\\anaconda3\\envs\\env1\\lib\\site-packages (from rich>=10.11.0->streamlit) (2.1.0)\n",
      "Requirement already satisfied: mdurl~=0.1 in c:\\users\\dell\\anaconda3\\envs\\env1\\lib\\site-packages (from markdown-it-py<3.0.0,>=2.1.0->rich>=10.11.0->streamlit) (0.1.2)\n",
      "Requirement already satisfied: tzdata in c:\\users\\dell\\anaconda3\\envs\\env1\\lib\\site-packages (from tzlocal>=1.1->streamlit) (2022.7)\n",
      "Requirement already satisfied: pytz-deprecation-shim in c:\\users\\dell\\anaconda3\\envs\\env1\\lib\\site-packages (from tzlocal>=1.1->streamlit) (0.1.0.post0)\n",
      "Requirement already satisfied: backports.zoneinfo in c:\\users\\dell\\anaconda3\\envs\\env1\\lib\\site-packages (from tzlocal>=1.1->streamlit) (0.2.1)\n",
      "Requirement already satisfied: decorator>=3.4.0 in c:\\users\\dell\\anaconda3\\envs\\env1\\lib\\site-packages (from validators>=0.2->streamlit) (5.1.1)\n"
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
