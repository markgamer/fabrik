import streamlit as st
import streamlit_toggle as tog
import os
import subprocess

def process_exists(process_name):
    call = 'TASKLIST', '/FI', 'imagename eq %s' % process_name
    output = subprocess.check_output(call).decode()
    last_line = output.strip().split('\r\n')[-1]
    return last_line.lower().startswith(process_name.lower())


def check_password():
    """Returns `True` if the user had the correct password."""

    def password_entered():
        """Checks whether a password entered by the user is correct."""
        if st.session_state["password"] == st.secrets["password"]:
            st.session_state["password_correct"] = True
            del st.session_state["password"]
        else:
            st.session_state["password_correct"] = False

    if "password_correct" not in st.session_state:

        st.text_input(
            "Password", type="password", on_change=password_entered, key="password"
        )
        return False
    elif not st.session_state["password_correct"]:

        st.text_input(
            "Password", type="password", on_change=password_entered, key="password"
        )
        st.error("😕 Password incorrect")
        return False
    else:

        return True


st.set_page_config(page_title='minceraft server',layout='wide')


if check_password():
    value=0

    with open('switch_value.txt') as f:
        value=f.readlines()

    switch=tog.st_toggle_switch(label="Start", 
                                    key="Key1", 
                                    default_value=eval(value[0]), 
                                    label_after=True, 
                                    inactive_color = '#D3D3D3', 
                                    active_color="#11567f", 
                                    track_color="#29B5E8")


    if switch and (value[0] != str(switch)):
        try:
            if not (process_exists("cmd.exe")):
                os.startfile("ngrok.bat")
                os.startfile("start.bat")
        except:
            pass

    if switch==False:
        try:
            process_exists("cmd.exe")
        except:
            os.system("taskkill /im cmd.exe")
            os.system("taskkill /im cmd.exe")
            os.system("taskkill /im cmd.exe")

    with open("switch_value.txt",'w') as f:
        f.write(str(switch))

    print(switch)