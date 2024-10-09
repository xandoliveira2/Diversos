const express = require('express')
const mongoose = require('mongoose')
const uri = 'mongodb://localhost/27017'
mongoose.connect(uri)

const model1 = mongoose.Schema({
    nome:String,
    idade:Number,
    observacao:String,

})

const modelo = mongoose.model('\?',model1)
// const modelo = mongoose.model('teste2',{nome:String,idade:Number}) ---> roda mas joga no lixo o resto da informação não especificada

const dado = new modelo({
    nome:'Alexandre1',
    idade:221,
    // curso:'Desen. Soft. Multi.1',
    // genero:'masculino1',
    observacao: 'THIS PIECE OF SHIT',
})

dado.save()