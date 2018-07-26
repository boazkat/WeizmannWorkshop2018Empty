from IPython.display import HTML
global sOpn,sEnd,svarx,svary,sdtms
def BallStart(x,y):
    global sOpn,sEnd,svarx,svary,sdtms,simulation
    file = open('BallAnimation/HTMLAnimationOpening.txt', 'r')
    sOpn=file.read()
    file.close()
    file = open('BallAnimation/HTMLAnimationEnding.txt', 'r')
    sEnd=file.read()
    file.close()
    svarx='\n var x=['+str(x)
    svary='\n var y=['+str(y)
def BallMoveTo(x,y):
    global svarx,svary
    svarx+=','+str(x)
    svary+=','+str(y)
def BallRun(dts=0.003):
    global sOpn,sEnd,svarx,svary,sdtms
    sdtms='\n var dtms='+'%.0f'%round(dts*1000)+';\n'
    svarx+=']; \n'
    svary+=']; \n'
    animation=sOpn+sdtms+svarx+svary+sEnd
    file = open('BallAnimation/HTMLAnimation.html', 'w+')
    file.write(animation)
    file.close()
    return animation
