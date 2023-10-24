from fastapi import FastAPI
import uvicorn
import source_code

app=FastAPI()

@app.get('/')
async def msg():
    return 'Server alive'

@app.post('/moviename')
async def recommend(movie):
    recommendation=source_code.recommended(movie)
    return recommendation

if __name__=='__main__':
    uvicorn.run(app, host='localhost', port=8002)