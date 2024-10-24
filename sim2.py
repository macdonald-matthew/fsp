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

def SHOT_SIM(A_Shooter1,S_Shooter1,
             A_Shooter2,S_Shooter2,
             A_Shooter3,S_Shooter3,
             A_Shooter4,S_Shooter4,
             A_Shooter5,S_Shooter5,
             A_Shooter6,S_Shooter6,
             A_Shooter7,S_Shooter7,
             A_Shooter8,S_Shooter8,
             A_Shooter9,S_Shooter9,
             A_Shooter10,S_Shooter10,
             Shields,Defense):
    winner=0  #No winner to start
    num_b_mis1=S_Shooter1
    num_b_mis2=S_Shooter2
    num_b_mis3=S_Shooter3
    num_b_mis4=S_Shooter4
    num_b_mis5=S_Shooter5
    num_b_mis6=S_Shooter6
    num_b_mis7=S_Shooter7
    num_b_mis8=S_Shooter8
    num_b_mis9=S_Shooter9
    num_b_mis10=S_Shooter10
    shields=Shields.copy()
    defense=Defense.copy()
    while winner==0: #keep going to Red or Blue wins
        if num_b_mis1>0:
            B_shoot1=random.randint(1, A_Shooter1)  #shooter shot value of it has shots remaining
            num_b_mis1-=1  #number of shots decreases by 1
            if shields:
                if B_shoot1>=shields[0]:  #if shot value is greater than shield value, number of shields decreases by one
                    shields.pop(0)
            else:  #if red is out of shiels, the shot goes agains the defense value
                if defense:
                    if B_shoot1>=defense[0]:  #if the shot value is greater than the defense value, the target is destroyed
                        defense.pop(0)
                    if not defense:
                        winner+=1
                        return("Shooter 1 destroyed Red", len(shields),len(defense))
            if da(A_Shooter1,B_shoot1):
                if shields:
                    if B_shoot1>=shields[0]:  #if shot value is greater than shield value, number of shields decreases by one
                        shields.pop(0)
                    else:  #if red is out of shiels, the shot goes agains the defense value
                        if defense:
                            if B_shoot1>=defense[0]:  #if the shot value is greater than the defense value, the target is destroyed
                                defense.pop(0)
                        else:
                            winner+=1
                            return("Shooter 1 destroyed Red", len(shields),len(defense))
                    
        elif num_b_mis2>0: #if the previous shooter runs out of shots, the next shooter start shooting
            B_shoot2=random.randint(1, A_Shooter2)  
            num_b_mis2-=1 
            if shields:
                if B_shoot2>=shields[0]:  #if shot value is greater than shield value, number of shields decreases by one
                    shields.pop(0)
            else:  #if red is out of shiels, the shot goes agains the defense value
                if defense:
                    if B_shoot2>=defense[0]:  #if the shot value is greater than the defense value, the target is destroyed
                        defense.pop(0)
                    if not defense:
                        winner+=1
                        return("Shooter 2 destroyed Red", len(shields),len(defense))
            if da(A_Shooter2,B_shoot2):
                if shields:
                    if B_shoot2>=shields[0]:  #if shot value is greater than shield value, number of shields decreases by one
                        shields.pop(0)
                    else:  #if red is out of shiels, the shot goes agains the defense value
                        if defense:
                            if B_shoot2>=defense[0]:  #if the shot value is greater than the defense value, the target is destroyed
                                defense.pop(0)
                        else:
                            winner+=1
                            return("Shooter 2 destroyed Red", len(shields),len(defense))
                    
        elif num_b_mis3>0:
            B_shoot3=random.randint(1, A_Shooter3) 
            num_b_mis3-=1  
            if shields:
                if B_shoot3>=shields[0]:  #if shot value is greater than shield value, number of shields decreases by one
                    shields.pop(0)
            else:  #if red is out of shiels, the shot goes agains the defense value
                if defense:
                    if B_shoot3>=defense[0]:  #if the shot value is greater than the defense value, the target is destroyed
                        defense.pop(0)
                    if not defense:
                        winner+=1
                        return("Shooter 3 destroyed Red", len(shields),len(defense))
            if da(A_Shooter3,B_shoot3):
                if shields:
                    if B_shoot3>=shields[0]:  #if shot value is greater than shield value, number of shields decreases by one
                        shields.pop(0)
                    else:  #if red is out of shiels, the shot goes agains the defense value
                        if defense:
                            if B_shoot3>=defense[0]:  #if the shot value is greater than the defense value, the target is destroyed
                                defense.pop(0)
                        else:
                            winner+=1
                            return("Shooter 3 destroyed Red", len(shields),len(defense))


        elif num_b_mis4>0:
            B_shoot4=random.randint(1, A_Shooter4) 
            num_b_mis4-=1  
            if shields:
                if B_shoot4>=shields[0]:  #if shot value is greater than shield value, number of shields decreases by one
                    shields.pop(0)
            else:  #if red is out of shiels, the shot goes agains the defense value
                if defense:
                    if B_shoot4>=defense[0]:  #if the shot value is greater than the defense value, the target is destroyed
                        defense.pop(0)
                    if not defense:
                        winner+=1
                        return("Shooter 4 destroyed Red", len(shields),len(defense))
            if da(A_Shooter4,B_shoot4):
                if shields:
                    if B_shoot4>=shields[0]:  #if shot value is greater than shield value, number of shields decreases by one
                        shields.pop(0)
                    else:  #if red is out of shiels, the shot goes agains the defense value
                        if defense:
                            if B_shoot4>=defense[0]:  #if the shot value is greater than the defense value, the target is destroyed
                                defense.pop(0)
                        else:
                            winner+=1
                            return("Shooter 4 destroyed Red", len(shields),len(defense))

        elif num_b_mis5>0:
            B_shoot5=random.randint(1, A_Shooter5)  
            num_b_mis5-=1  
            if shields:
                if B_shoot5>=shields[0]:  #if shot value is greater than shield value, number of shields decreases by one
                    shields.pop(0)
            else:  #if red is out of shiels, the shot goes agains the defense value
                if defense:
                    if B_shoot5>=defense[0]:  #if the shot value is greater than the defense value, the target is destroyed
                        defense.pop(0)
                    if not defense:
                        winner+=1
                        return("Shooter 5 destroyed Red", len(shields),len(defense))
            if da(A_Shooter5,B_shoot5):
                if shields:
                    if B_shoot5>=shields[0]:  #if shot value is greater than shield value, number of shields decreases by one
                        shields.pop(0)
                    else:  #if red is out of shiels, the shot goes agains the defense value
                        if defense:
                            if B_shoot5>=defense[0]:  #if the shot value is greater than the defense value, the target is destroyed
                                defense.pop(0)
                        else:
                            winner+=1
                            return("Shooter 5 destroyed Red", len(shields),len(defense))

        elif num_b_mis6>0:
            B_shoot6=random.randint(1, A_Shooter6)  
            num_b_mis6-=1 
            if shields:
                if B_shoot6>=shields[0]:  #if shot value is greater than shield value, number of shields decreases by one
                    shields.pop(0)
            else:  #if red is out of shiels, the shot goes agains the defense value
                if defense:
                    if B_shoot6>=defense[0]:  #if the shot value is greater than the defense value, the target is destroyed
                        defense.pop(0)
                    if not defense:
                        winner+=1
                        return("Shooter 6 destroyed Red", len(shields),len(defense))
            if da(A_Shooter6,B_shoot6):
                if shields:
                    if B_shoot6>=shields[0]:  #if shot value is greater than shield value, number of shields decreases by one
                        shields.pop(0)
                    else:  #if red is out of shiels, the shot goes agains the defense value
                        if defense:
                            if B_shoot6>=defense[0]:  #if the shot value is greater than the defense value, the target is destroyed
                                defense.pop(0)
                        else:
                            winner+=1
                            return("Shooter 6 destroyed Red", len(shields),len(defense))

        elif num_b_mis7>0:
            B_shoot7=random.randint(1, A_Shooter7)
            num_b_mis7-=1  
            if shields:
                if B_shoot7>=shields[0]:  #if shot value is greater than shield value, number of shields decreases by one
                    shields.pop(0)
            else:  #if red is out of shiels, the shot goes agains the defense value
                if defense:
                    if B_shoot7>=defense[0]:  #if the shot value is greater than the defense value, the target is destroyed
                        defense.pop(0)
                    if not defense:
                        winner+=1
                        return("Shooter 7 destroyed Red", len(shields),len(defense))
            if da(A_Shooter7,B_shoot7):
                if shields:
                    if B_shoot7>=shields[0]:  #if shot value is greater than shield value, number of shields decreases by one
                        shields.pop(0)
                    else:  #if red is out of shiels, the shot goes agains the defense value
                        if defense:
                            if B_shoot7>=defense[0]:  #if the shot value is greater than the defense value, the target is destroyed
                                defense.pop(0)
                        else:
                            winner+=1
                            return("Shooter 7 destroyed Red", len(shields),len(defense))

        elif num_b_mis8>0:
            B_shoot8=random.randint(1, A_Shooter8)  
            num_b_mis8-=1  
            if shields:
                if B_shoot8>=shields[0]:  #if shot value is greater than shield value, number of shields decreases by one
                    shields.pop(0)
            else:  #if red is out of shiels, the shot goes agains the defense value
                if defense:
                    if B_shoot8>=defense[0]:  #if the shot value is greater than the defense value, the target is destroyed
                        defense.pop(0)
                    if not defense:
                        winner+=1
                        return("Shooter 8 destroyed Red", len(shields),len(defense))
            if da(A_Shooter8,B_shoot8):
                if shields:
                    if B_shoot8>=shields[0]:  #if shot value is greater than shield value, number of shields decreases by one
                        shields.pop(0)
                    else:  #if red is out of shiels, the shot goes agains the defense value
                        if defense:
                            if B_shoot8>=defense[0]:  #if the shot value is greater than the defense value, the target is destroyed
                                defense.pop(0)
                        else:
                            winner+=1
                            return("Shooter 8 destroyed Red", len(shields),len(defense))

        elif num_b_mis9>0:
            B_shoot9=random.randint(1, A_Shooter9) 
            num_b_mis9-=1  
            if shields:
                if B_shoot9>=shields[0]:  #if shot value is greater than shield value, number of shields decreases by one
                    shields.pop(0)
            else:  #if red is out of shiels, the shot goes agains the defense value
                if defense:
                    if B_shoot9>=defense[0]:  #if the shot value is greater than the defense value, the target is destroyed
                        defense.pop(0)
                    if not defense:
                        winner+=1
                        return("Shooter 9 destroyed Red", len(shields),len(defense))
            if da(A_Shooter9,B_shoot9):
                if shields:
                    if B_shoot9>=shields[0]:  #if shot value is greater than shield value, number of shields decreases by one
                        shields.pop(0)
                    else:  #if red is out of shiels, the shot goes agains the defense value
                        if defense:
                            if B_shoot9>=defense[0]:  #if the shot value is greater than the defense value, the target is destroyed
                                defense.pop(0)
                        else:
                            winner+=1
                            return("Shooter 9 destroyed Red", len(shields),len(defense))

        elif num_b_mis10>0:
            B_shoot10=random.randint(1, A_Shooter10) 
            num_b_mis10-=1 
            if shields:
                if B_shoot10>=shields[0]:  #if shot value is greater than shield value, number of shields decreases by one
                    shields.pop(0)
            else:  #if red is out of shiels, the shot goes agains the defense value
                if defense:
                    if B_shoot10>=defense[0]:  #if the shot value is greater than the defense value, the target is destroyed
                        defense.pop(0)
                    if not defense:
                        winner+=1
                        return("Shooter 10 destroyed Red", len(shields),len(defense))
            if da(A_Shooter10,B_shoot10):
                if shields:
                    if B_shoot10>=shields[0]:  #if shot value is greater than shield value, number of shields decreases by one
                        shields.pop(0)
                    else:  #if red is out of shiels, the shot goes agains the defense value
                        if defense:
                            if B_shoot10>=defense[0]:  #if the shot value is greater than the defense value, the target is destroyed
                                defense.pop(0)
                        else:
                            winner+=1
                            return("Shooter 10 destroyed Red", len(shields),len(defense))


        else: #if all shooters are out of shots the traget survives
            winner+=1
            return("Out of shots", len(shields),len(defense))   
        
######SIMULATION TRIALS##########
n=10000
dice=[4,6,8,10,12,16,20]
st.title("Shot Simulator")
st.write("Attacker Information")
# Create a dropdown
selected_shooters = st.selectbox("Enter number of Shooters", [1,2,3,4,5,6,7,8,9,10])        
n_shooters = selected_shooters        
if n_shooters>=1:
    A_Shooter1=st.selectbox("Enter shooter 1's Attack Value", dice)
    S_Shooter1=st.number_input('Enter number of shots for Shooter 1',value=0,min_value=0, step=1)
else:
    A_Shooter1=1
    S_Shooter1=0
if n_shooters>=2:
    A_Shooter2=st.selectbox("Enter shooter 2's Attack Value", dice)
    S_Shooter2=st.number_input('Enter number of shots for Shooter 2',value=0,min_value=0, step=1)
else:
    A_Shooter2=1
    S_Shooter2=0
if n_shooters>=3:
    A_Shooter3=st.selectbox("Enter shooter 3's Attack Value", dice)
    S_Shooter3=st.number_input('Enter number of shots for Shooter 3',value=0,min_value=0, step=1)
else:
    A_Shooter3=1
    S_Shooter3=0
if n_shooters>=4:
    A_Shooter4=st.selectbox("Enter shooter 4's Attack Value", dice)
    S_Shooter4=st.number_input('Enter number of shots for Shooter 4',value=0,min_value=0, step=1)
else:
    A_Shooter4=1
    S_Shooter4=0
if n_shooters>=5:
    A_Shooter5=st.selectbox("Enter shooter 5's Attack Value", dice)
    S_Shooter5=st.number_input('Enter number of shots for Shooter 5',value=0,min_value=0, step=1)
else:
    A_Shooter5=1
    S_Shooter5=0
if n_shooters>=6:
    A_Shooter6=st.selectbox("Enter shooter 6's Attack Value", dice)
    S_Shooter6=st.number_input('Enter number of shots for Shooter 6',value=0,min_value=0, step=1)
else:
    A_Shooter6=1
    S_Shooter6=0
if n_shooters>=7:
    A_Shooter7=st.selectbox("Enter shooter 7's Attack Value", dice)
    S_Shooter7=st.number_input('Enter number of shots for Shooter 7',value=0,min_value=0, step=1)
else:
    A_Shooter7=1
    S_Shooter7=0
if n_shooters>=8:
    A_Shooter8=st.selectbox("Enter shooter 8's Attack Value", dice)
    S_Shooter8=st.number_input('Enter number of shots for Shooter 8',value=0,min_value=0, step=1)
else:
    A_Shooter8=1
    S_Shooter8=0
if n_shooters>=9:
    A_Shooter9=st.selectbox("Enter shooter 9's Attack Value", dice)
    S_Shooter9=st.number_input('Enter number of shots for Shooter 9',value=0,min_value=0, step=1)
else:
    A_Shooter9=1
    S_Shooter9=0
if n_shooters>=10:
    A_Shooter10=st.selectbox("Enter shooter 10's Attack Value", dice)
    S_Shooter10=st.number_input('Enter number of shots for Shooter 10',value=0,min_value=0, step=1)
else:
    A_Shooter10=1
    S_Shooter10=0

st.write("Defender Information") 
N_Shields=st.number_input("Enter number of defender’s shields",value=0,min_value=0, step=1)       
S_Shields=st.number_input("Enter strength of defender’s shields",value=0,min_value=0, step=1)  
Defense_step=st.number_input("Enter the number of defender's deffesnive steps including suppression",value=1,min_value=1, step=1)
Defense_val=st.selectbox("Enter defender’s defense value",dice)
Defense=[Defense_val]*Defense_step

st.write("Cooperative Defender Information") 
CD=st.selectbox("Enter number of units are providing cooperative defense", [0,1,2,3,4,5,6,7,8,9,10])
Shields=[S_Shields]*N_Shields

if CD>=1:
    D1N=st.number_input("Enter number of shields from first coopeartive defender",value=0,min_value=0, step=1)
    D1=st.number_input("Enter first cooperative defender's shield value",value=0,min_value=0, step=1)
    Shields=sorted(Shields+[D1]*D1N)
if CD>=2:
    D2N=st.number_input("Enter number of shields from second coopeartive defender",value=0,min_value=0, step=1)
    D2=st.number_input("Enter second cooperative defender's shield value",value=0,min_value=0, step=1)
    Shields=sorted(Shields+[D2]*D2N)
if CD>=3:
    D3N=st.number_input("Enter number of shields from third coopeartive defender",value=0,min_value=0, step=1)
    D3=st.number_input("Enter third cooperative defender's shield value",value=0,min_value=0, step=1)
    Shields=sorted(Shields+[D3]*D3N)
if CD>=4:
    D4N=st.number_input("Enter number of shields from fourth coopeartive defender",value=0,min_value=0, step=1)
    D4=st.number_input("Enter fourth cooperative defender's shield value",value=0,min_value=0, step=1)
    Shields=sorted(Shields+[D4]*D4N)
if CD>=5:
    D5N=st.number_input("Enter number of shields from fifth coopeartive defender",value=0,min_value=0, step=1)
    D5=st.number_input("Enter fifth cooperative defender's shield value",value=0,min_value=0, step=1)
    Shields=sorted(Shields+[D5]*D5N)
if CD>=6:
    D6N=st.number_input("Enter number of shields from sixth coopeartive defender",value=0,min_value=0, step=1)
    D6=st.number_input("Enter sixth cooperative defender's shield value",value=0,min_value=0, step=1)
    Shields=sorted(Shields+[D6]*D6N)
if CD>=7:
    D7N=st.number_input("Enter number of shields from seventh coopeartive defender",value=0,min_value=0, step=1)
    D7=st.number_input("Enter seventh cooperative defender's shield value",value=0,min_value=0, step=1)
    Shields=sorted(Shields+[D7]*D7N)
if CD>=8:
    D8N=st.number_input("Enter number of shields from eigth coopeartive defender",value=0,min_value=0, step=1)
    D8=st.number_input("Enter eigth cooperative defender's shield value",value=0,min_value=0, step=1)
    Shields=sorted(Shields+[D8]*D8N)
if CD>=9:
    D9N=st.number_input("Enter number of shields from ninth coopeartive defender",value=0,min_value=0, step=1)
    D9=st.number_input("Enter ninth cooperative defender's shield value",value=0,min_value=0, step=1)
    Shields=sorted(Shields+[D9]*D9N)
if CD>=10:
    D10N=st.number_input("Enter number of shields from tenth coopeartive defender",value=0,min_value=0, step=1)
    D10=st.number_input("Enter tenth cooperative defender's shield value",value=0,min_value=0, step=1)
    Shields=sorted(Shields+[D10]*D10N)

Blue_Wins=0
Red_Wins=0
Blue1_Wins=0
Blue2_Wins=0
Blue3_Wins=0
Blue4_Wins=0
Blue5_Wins=0
Blue6_Wins=0
Blue7_Wins=0
Blue8_Wins=0
Blue9_Wins=0
Blue10_Wins=0
smain=[]
dmain=[]
for i in range(n):
    sim, s, d= SHOT_SIM(A_Shooter1,S_Shooter1,
             A_Shooter2,S_Shooter2,
             A_Shooter3,S_Shooter3,
             A_Shooter4,S_Shooter4,
             A_Shooter5,S_Shooter5,
             A_Shooter6,S_Shooter6,
             A_Shooter7,S_Shooter7,
             A_Shooter8,S_Shooter8,
             A_Shooter9,S_Shooter9,
             A_Shooter10,S_Shooter10,
             Shields,Defense)
    if sim=="Shooter 1 destroyed Red":
        Blue_Wins+=1
        Blue1_Wins+=1
        smain.append(s)
        dmain.append(d)
    if sim=="Shooter 2 destroyed Red":
        Blue_Wins+=1
        Blue2_Wins+=1
        smain.append(s)
        dmain.append(d)
    if sim=="Shooter 3 destroyed Red":
        Blue_Wins+=1
        Blue3_Wins+=1
        smain.append(s)
        dmain.append(d)
    if sim=="Shooter 4 destroyed Red":
        Blue_Wins+=1
        Blue4_Wins+=1
        smain.append(s)
        dmain.append(d)
    if sim=="Shooter 5 destroyed Red":
        Blue_Wins+=1
        Blue5_Wins+=1
        smain.append(s)
        dmain.append(d)
    if sim=="Shooter 6 destroyed Red":
        Blue_Wins+=1
        Blue6_Wins+=1
        smain.append(s)
        dmain.append(d)
    if sim=="Shooter 7 destroyed Red":
        Blue_Wins+=1
        Blue7_Wins+=1
        smain.append(s)
        dmain.append(d)
    if sim=="Shooter 8 destroyed Red":
        Blue_Wins+=1
        Blue8_Wins+=1
        smain.append(s)
        dmain.append(d)
    if sim=="Shooter 9 destroyed Red":
        Blue_Wins+=1
        Blue9_Wins+=1
        smain.append(s)
        dmain.append(d)
    if sim=="Shooter 10 destroyed Red":
        Blue_Wins+=1
        Blue10_Wins+=1
        smain.append(s)
        dmain.append(d)
    if sim=="Out of shots":
        Red_Wins+=1
        smain.append(s)
        dmain.append(d)

st.write("Blue's Win Percent:", round(100*Blue_Wins/n))
if n_shooters>=1:
    st.write("Percent of iterations that shooter 1 destroyed red:", round(100*Blue1_Wins/n))
if n_shooters>=2:    
    st.write("Percent of iterations that shooter 2 destroyed red:", round(100*Blue2_Wins/n))
if n_shooters>=3:    
    st.write("Percent of iterations that shooter 3 destroyed red:", round(100*Blue3_Wins/n))
if n_shooters>=4:    
    st.write("Percent of iterations that shooter 4 destroyed red:", round(100*Blue4_Wins/n))
if n_shooters>=5:    
    st.write("Percent of iterations that shooter 5 destroyed red:", round(100*Blue5_Wins/n))
if n_shooters>=6:    
    st.write("Percent of iterations that shooter 6 destroyed red:", round(100*Blue6_Wins/n))
if n_shooters>=7:    
    st.write("Percent of iterations that shooter 7 destroyed red:", round(100*Blue7_Wins/n))
if n_shooters>=8:    
    st.write("Percent of iterations that shooter 8 destroyed red:", round(100*Blue8_Wins/n))
if n_shooters>=9:    
    st.write("Percent of iterations that shooter 9 destroyed red:", round(100*Blue9_Wins/n))
if n_shooters>=10:    
    st.write("Percent of iterations that shooter 10 destroyed red:", round(100*Blue10_Wins/n))

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
fig.update_xaxes(title_text='Deffesnive Steps Remaining')
fig.update_yaxes(title_text='Percent Observed')

fig.update_layout(
    title={
        'text': "Histogram of Deffesnive Steps Remaining",
        'font': {'size': 20},
        'xanchor': 'center' 
        
        # Adjust the font size as needed
    }, showlegend=False, hovermode=False,title_x=0.5)

st.plotly_chart(fig)

