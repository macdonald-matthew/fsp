import streamlit as st
import random
import plotly.express as px
#####SIMULATION SETUP########

# A_Shootern: shooter n's attack value
# S_Shootern: number of shots that shooter n takes
# N_Shields:  Number of shields
# S_Shields:  Shield strength
# Defense:  Defense value

def da(a1,a2):
    return(a1==12 and a2==12 or a1==16 and a2==16 or a1==20 and a2==20)

def SHOT_SIM(Dice,
             Shields,Defense):
    winner=0  #No winner to start
    shots=Dice.copy()
    shields=Shields.copy()
    steps=Defense.copy()
    while winner==0: #keep going to Red or Blue wins
        for i in range(len(shots)):
            if shots:
                if shields:
                    if [x for x in shots if x>= shields[0]]:
                        shots.pop(shots.index(min([x for x in shots if x>= shields[0]])))
                        shields.pop(0) 
                if not shields:
                    if steps:
                        if [x for x in shots if x>= steps[0]]:
                            shots.pop(shots.index(min([x for x in shots if x>= steps[0]])))
                            steps.pop(0)
        if shields:
            winner+=1
            return("Red Wins", len(shields), len(steps))
        elif steps:
            winner+=1
            return("Red Wins", len(shields), len(steps))
        else:
            winner+=1
            return("Blue Wins", len(shields), len(steps))
        
######SIMULATION TRIALS##########
n=10000
dice=[4,6,8,10,12,16,20]
st.title("Shot Simulator")
st.write("Attacker Information")
# Create a dropdown
selected_shooters = st.selectbox("Enter number of Shooters", [1,2,3,4,5,6,7,8,9,10])        
n_shooters = selected_shooters  
Attack=[]
if n_shooters>=1:
    A_Shooter1=st.selectbox("Enter shooter 1's Attack Value", dice)
    S_Shooter1=st.number_input('Enter number of shots for Shooter 1',value=0,min_value=0, step=1)
    Attack=Attack+[A_Shooter1]*S_Shooter1

if n_shooters>=2:
    A_Shooter2=st.selectbox("Enter shooter 2's Attack Value", dice)
    S_Shooter2=st.number_input('Enter number of shots for Shooter 2',value=0,min_value=0, step=1)
    Attack=Attack+[A_Shooter2]*S_Shooter2

if n_shooters>=3:
    A_Shooter3=st.selectbox("Enter shooter 3's Attack Value", dice)
    S_Shooter3=st.number_input('Enter number of shots for Shooter 3',value=0,min_value=0, step=1)
    Attack=Attack+[A_Shooter3]*S_Shooter3

if n_shooters>=4:
    A_Shooter4=st.selectbox("Enter shooter 4's Attack Value", dice)
    S_Shooter4=st.number_input('Enter number of shots for Shooter 4',value=0,min_value=0, step=1)
    Attack=Attack+[A_Shooter4]*S_Shooter4

if n_shooters>=5:
    A_Shooter5=st.selectbox("Enter shooter 5's Attack Value", dice)
    S_Shooter5=st.number_input('Enter number of shots for Shooter 5',value=0,min_value=0, step=1)
    Attack=Attack+[A_Shooter5]*S_Shooter5

if n_shooters>=6:
    A_Shooter6=st.selectbox("Enter shooter 6's Attack Value", dice)
    S_Shooter6=st.number_input('Enter number of shots for Shooter 6',value=0,min_value=0, step=1)
    Attack=Attack+[A_Shooter6]*S_Shooter6

if n_shooters>=7:
    A_Shooter7=st.selectbox("Enter shooter 7's Attack Value", dice)
    S_Shooter7=st.number_input('Enter number of shots for Shooter 7',value=0,min_value=0, step=1)
    Attack=Attack+[A_Shooter7]*S_Shooter7

if n_shooters>=8:
    A_Shooter8=st.selectbox("Enter shooter 8's Attack Value", dice)
    S_Shooter8=st.number_input('Enter number of shots for Shooter 8',value=0,min_value=0, step=1)
    Attack=Attack+[A_Shooter8]*S_Shooter8

if n_shooters>=9:
    A_Shooter9=st.selectbox("Enter shooter 9's Attack Value", dice)
    S_Shooter9=st.number_input('Enter number of shots for Shooter 9',value=0,min_value=0, step=1)
    Attack=Attack+[A_Shooter9]*S_Shooter9

if n_shooters>=10:
    A_Shooter10=st.selectbox("Enter shooter 10's Attack Value", dice)
    S_Shooter10=st.number_input('Enter number of shots for Shooter 10',value=0,min_value=0, step=1)
    Attack=Attack+[A_Shooter10]*S_Shooter10


st.write("Defender Information") 
N_Shields=st.number_input("Enter number of defender’s shields",value=0,min_value=0, step=1)       
S_Shields=st.number_input("Enter strength of defender’s shields",value=0,min_value=0, step=1)  
Defense_step=st.number_input("Enter the number of defender's steps",value=1,min_value=1, step=1)
Defense_val=st.number_input("Enter defender’s defense value",value=0,min_value=0, step=1)
Defense=sorted([Defense_val]*Defense_step)

st.write("Cooperative Defender Information") 
CD=st.selectbox("Enter number of units are providing cooperative defense", [0,1,2,3,4,5,6,7,8,9,10])
Shields=[S_Shields]*N_Shields

if CD>=1:
    D1N=st.number_input("Enter number of shields from first cooperative defender",value=0,min_value=0, step=1)
    D1=st.number_input("Enter first cooperative defender's shield value",value=0,min_value=0, step=1)
    Shields=sorted(Shields+[D1]*D1N)
if CD>=2:
    D2N=st.number_input("Enter number of shields from second cooperative defender",value=0,min_value=0, step=1)
    D2=st.number_input("Enter second cooperative defender's shield value",value=0,min_value=0, step=1)
    Shields=sorted(Shields+[D2]*D2N)
if CD>=3:
    D3N=st.number_input("Enter number of shields from third cooperative defender",value=0,min_value=0, step=1)
    D3=st.number_input("Enter third cooperative defender's shield value",value=0,min_value=0, step=1)
    Shields=sorted(Shields+[D3]*D3N)
if CD>=4:
    D4N=st.number_input("Enter number of shields from fourth cooperative defender",value=0,min_value=0, step=1)
    D4=st.number_input("Enter fourth cooperative defender's shield value",value=0,min_value=0, step=1)
    Shields=sorted(Shields+[D4]*D4N)
if CD>=5:
    D5N=st.number_input("Enter number of shields from fifth cooperative defender",value=0,min_value=0, step=1)
    D5=st.number_input("Enter fifth cooperative defender's shield value",value=0,min_value=0, step=1)
    Shields=sorted(Shields+[D5]*D5N)
if CD>=6:
    D6N=st.number_input("Enter number of shields from sixth cooperative defender",value=0,min_value=0, step=1)
    D6=st.number_input("Enter sixth cooperative defender's shield value",value=0,min_value=0, step=1)
    Shields=sorted(Shields+[D6]*D6N)
if CD>=7:
    D7N=st.number_input("Enter number of shields from seventh cooperative defender",value=0,min_value=0, step=1)
    D7=st.number_input("Enter seventh cooperative defender's shield value",value=0,min_value=0, step=1)
    Shields=sorted(Shields+[D7]*D7N)
if CD>=8:
    D8N=st.number_input("Enter number of shields from eigth cooperative defender",value=0,min_value=0, step=1)
    D8=st.number_input("Enter eigth cooperative defender's shield value",value=0,min_value=0, step=1)
    Shields=sorted(Shields+[D8]*D8N)
if CD>=9:
    D9N=st.number_input("Enter number of shields from ninth cooperative defender",value=0,min_value=0, step=1)
    D9=st.number_input("Enter ninth cooperative defender's shield value",value=0,min_value=0, step=1)
    Shields=sorted(Shields+[D9]*D9N)
if CD>=10:
    D10N=st.number_input("Enter number of shields from tenth cooperative defender",value=0,min_value=0, step=1)
    D10=st.number_input("Enter tenth cooperative defender's shield value",value=0,min_value=0, step=1)
    Shields=sorted(Shields+[D10]*D10N)

Blue_Wins=0
Red_Wins=0
smain=[]
dmain=[]
for i in range(n):
    d=[]
    dt=[]
    for i in range(len(Attack)):
        d.append(random.randint(1, Attack[i]))
        if da(d[i],Attack[i]):
            dt.append(Attack[i])
    Dice=d+dt
    sim, s, d= SHOT_SIM(Dice,
             Shields,Defense)
    if sim=="Red Wins":
        Red_Wins+=1
        smain.append(s)
        dmain.append(d)
    if sim=="Blue Wins":
        Blue_Wins+=1
        smain.append(s)
        dmain.append(d)

st.write("Chance to destroy target:  ", round(100*Blue_Wins/n),"%")

fig = px.histogram(smain, histnorm='percent')
fig.update_xaxes(title_text='Shields Remaining')
fig.update_yaxes(title_text='Percent Observed')

fig.update_layout(
    title={
        'text': "Histogram of Shields Remaining",
        'font': {'size': 20},
        'xanchor': 'center' 
        
        # Adjust the font size as needed
    }, showlegend=False, hovermode=False,title_x=0.5)

st.plotly_chart(fig)

fig = px.histogram(dmain, histnorm='percent')
fig.update_xaxes(title_text='Defensive Steps Remaining')
fig.update_yaxes(title_text='Percent Observed')

fig.update_layout(
    title={
        'text': "Histogram of Deffesnive Steps Remaining",
        'font': {'size': 20},
        'xanchor': 'center' 
        
        # Adjust the font size as needed
    }, showlegend=False, hovermode=False,title_x=0.5)
st.plotly_chart(fig)
