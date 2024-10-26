// import { createServer } from 'node:http'
// const server = createServer((request,response)=>{
    
//     console.log('oi')
   
//     response.write('<h1>Ola mundo</h1>')
//     response.write('outra tag lol<br/>')
//     response.write('ola mundo 3?')
    
  
//     return response.end()
// }
// )
// server.listen(3333)
// //localhost:3333
// GET - pegar 
// POST - criar
// PUT - atualizar/modificar
// DELETE - excluir 
// PATCH - alterar algo especifico de algum dado especifico
// projeto de criação de uma plataforma de video


import { fastify } from "fastify";
import { DatabaseMemory } from './database-memory.js';
const server = fastify()
const dataBase = new DatabaseMemory()
// Request Body
server.post('/videos',
    (request , response)=>{
        const {title,description,duration} = request.body
 
        console.log(request.body)
        dataBase.create({
            Title:title,
            description, //quando o nome do campo é o mesmo do dado, podemos incurtar isso usando 'short sintax' que é basicamente deixar só o nome
            duration, // description, e duration, é a mesma coisa que description : description,
        })
        
        
        
        return response.status(201).send() // 201 -> algo foi criado 
    }
)
server.get('/videos',
    ()=>{
        const videos = dataBase.list()
        console.log(videos)
        return videos
    }
)
server.put('/videos/:id', //para atualizar temos que atualizar um item em especifico, passando assim vai reconhecer que precisa de
    //mais um parametro (id) para 'atualizar'
    (request,response)=>{
        const videoID = request.params.id
        const {title,description,duration} = request.body

        dataBase.update(videoID,{
            Title:title,
            description,
            duration,
        })
        return response.status(204).send()
    }
)
server.delete('/videos/:id',
    (request,response)=>{
        const videoID = request.params.id
        dataBase.delete(videoID)
        response.status(204).send()
    }
)



// server.get('/', //se ele estiver na raiz (localhost)
//      ()=>{ //execute essa funcao
//         return "Hello World"
//     }
// )
// server.get('/teste1', //se ele estiver no local teste1
//      ()=>{ //execute essa funcao
//         return "IDFC"
//     }
// )
// server.get('/teste2', //se ele estiver na raiz (localhost)
//      ()=>{ //execute essa funcao
//         return "This will be wonderful"
//     }
// )
server.listen(
    {
    port:3333,
    }
)