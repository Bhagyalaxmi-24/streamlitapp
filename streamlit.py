{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "76a82738-dbd2-4e8c-8e63-622ed4a47785",
   "metadata": {},
   "outputs": [],
   "source": [
    "import streamlit as st\n",
    "from sklearn.datasets import load_iris\n",
    "from sklearn.model_selection import train_test_split\n",
    "from sklearn.ensemble import RandomForestClassifier"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "80c95ade-e901-43d2-96e4-b86d9a0bcb52",
   "metadata": {},
   "outputs": [],
   "source": [
    "iris=load_iris()\n",
    "\n",
    "X_train,X_test,y_train,y_test=train_test_split(\n",
    "    iris.data,\n",
    "    iris.target,\n",
    "    test_size=0.2,\n",
    "    random_state=42\n",
    ")\n",
    "model=RandomForestClassifier(random_state=42)\n",
    "model.fit(X_train,y_train)\n",
    "accuracy=model.score(X_test,y_test)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "40ad18a6-dc1a-4dd8-a20f-881a8053245c",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "2026-08-24 23:31:58.756 WARNING streamlit.runtime.scriptrunner_utils.script_run_context: Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-08-24 23:31:58.757 WARNING streamlit.runtime.scriptrunner_utils.script_run_context: Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-08-24 23:31:58.798 \n",
      "  \u001b[33m\u001b[1mWarning:\u001b[0m to view this Streamlit app on a browser, run it with the following\n",
      "  command:\n",
      "\n",
      "    streamlit run C:\\Users\\bhagy\\AppData\\Local\\Programs\\Python\\Python314\\Lib\\site-packages\\ipykernel_launcher.py [ARGUMENTS]\n",
      "2026-08-24 23:31:58.799 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-08-24 23:31:58.800 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-08-24 23:31:58.800 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-08-24 23:31:58.801 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-08-24 23:31:58.802 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-08-24 23:31:58.803 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-08-24 23:31:58.804 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-08-24 23:31:58.805 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-08-24 23:31:58.806 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-08-24 23:31:58.807 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-08-24 23:31:58.808 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "DeltaGenerator()"
      ]
     },
     "execution_count": 11,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "st.set_page_config(\n",
    "    page_title='Iris Flower Classifier',\n",
    "    page_icon='@#$',\n",
    "    layout='centered'\n",
    ")\n",
    "st.title('Iris Species Flower Classifier')\n",
    "st.write('Enter the measurement and click on **predict** to find the species')\n",
    "st.write(f'Measurement Accuracy ** {accuracy:.2%}')\n",
    "st.divider()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "e632496b-64f0-4118-ad6b-9ef2747d6ed6",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "2026-08-24 23:35:08.247 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-08-24 23:35:08.249 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-08-24 23:35:08.251 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-08-24 23:35:08.252 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-08-24 23:35:08.253 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-08-24 23:35:08.254 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-08-24 23:35:08.255 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-08-24 23:35:08.256 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-08-24 23:35:08.259 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-08-24 23:35:08.260 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-08-24 23:35:08.261 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-08-24 23:35:08.262 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-08-24 23:35:08.263 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-08-24 23:35:08.263 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-08-24 23:35:08.264 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-08-24 23:35:08.265 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-08-24 23:35:08.267 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-08-24 23:35:08.268 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-08-24 23:35:08.269 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-08-24 23:35:08.271 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-08-24 23:35:08.271 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-08-24 23:35:08.272 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-08-24 23:35:08.273 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-08-24 23:35:08.274 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n"
     ]
    }
   ],
   "source": [
    "sepal_length=st.number_input(\n",
    "    'Sepal length(cm)',\n",
    "    min_value=0.0,\n",
    "    max_value=10.0,\n",
    "    value=5.4\n",
    ")\n",
    "\n",
    "sepal_width=st.number_input(\n",
    "    'Sepal Width (cm)',\n",
    "    min_value=0.0,\n",
    "    max_value=10.0,\n",
    "    value=3.2\n",
    ")\n",
    "petal_length=st.number_input(\n",
    "    'petal length (cm)',\n",
    "    min_value=0.0,\n",
    "    max_value=10.0,\n",
    "    value=1.4\n",
    ")\n",
    "petal_width=st.number_input(\n",
    "    'petal width cm',\n",
    "    min_value=0.0,\n",
    "    max_value=10.0,\n",
    "    value=0.2\n",
    ")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "id": "9f228a3b-ad32-4393-bd60-a235736d27b1",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "2026-08-24 23:50:18.387 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-08-24 23:50:18.390 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-08-24 23:50:18.397 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-08-24 23:50:18.399 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-08-24 23:50:18.400 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n"
     ]
    }
   ],
   "source": [
    "if st.button('Predict Species'):\n",
    "    prediction=model.predict([[\n",
    "        \n",
    "        sepal_length,\n",
    "        sepal_width,\n",
    "        petal_length,\n",
    "        petal_width\n",
    "    ]])\n",
    "    probability=model.predict_proba([[\n",
    "        sepal_length,\n",
    "        sepal_width,\n",
    "        petal_length,\n",
    "        petal_width\n",
    "        \n",
    "    ]])\n",
    "\n",
    "    species=iris.target_names[prediction[0]]\n",
    "    st.success('prediction **{species.upper()}**')\n",
    "    st.subheader('Prediction Confidence')\n",
    "    st.write({\n",
    "        iris.target_names[i]:f\"{probability[0][i]*100:.2f}%\"\n",
    "            for i in range (len(iris.target_names))\n",
    "    })\n",
    "    st.progress(float(max(probability[0])))\n",
    "    st.divider()\n",
    "    st.caption(\"Developed by Streamlit and Scikit-learn\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "dd24b037-87f8-497c-a78b-e66afbff6ea4",
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
   "version": "3.14.6"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
