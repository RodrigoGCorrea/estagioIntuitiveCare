<template>
<div class="app">
  <div class="container">
    <input v-model="searching" placeholder="Digite o que quer pesquisar" />

    <select name="column" id="column" v-model="column">
      <option value="RegistroANS">RegistroANS</option>
      <option value="CNPJ">CNPJ</option>
      <option value="RazaoSocial">RazaoSocial</option>
      <option value="NomeFantasia">NomeFantasia</option>
      <option value="Modalidade">Modalidade</option>
      <option value="Logradouro">Logradouro</option>
      <option value="Numero">Numero</option>
      <option value="Complemento">Complemento</option>
      <option value="Bairro">Bairro</option>
      <option value="Cidade">Cidade</option>
      <option value="UF">UF</option>
      <option value="CEP">CEP</option>
      <option value="DDD">DDD</option>
      <option value="Telefone">Telefone</option>
      <option value="Fax">Fax</option>
      <option value="EnderecoEletronico">EnderecoEletronico</option>
      <option value="Representante">Representante</option>
      <option value="CargoRepresentante">CargoRepresentante</option>
      <option value="DataRegistroANS">DataRegistroANS</option>
    </select>

    <button @click="getData" class="btn btn-secondary">Pesquisar</button>
    </div>
    <div v-if="answer === 'start'"></div>
    <div v-else-if="answer.length > 0" class="table table-responsive mw-80">
      <table class="table table-striped table-bordered">
        <thead class="thead">
          <tr>
            <th>RegistroANS</th>
            <th>CNPJ</th>
            <th>RazaoSocial</th>
            <th>NomeFantasia</th>
            <th>Modalidade</th>
            <th>Logradouro</th>
            <th>Numero</th>
            <th>Complemento</th>
            <th>Bairro</th>
            <th>Cidade</th>
            <th>UF</th>
            <th>CEP</th>
            <th>DDD</th>
            <th>Telefone</th>
            <th>Fax</th>
            <th>EnderecoEletronico</th>
            <th>Representante</th>
            <th>CargoRepresentante</th>
            <th>DataRegistroANS</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="row of answer" :key="row.id" >
            <td v-for="element of row" :key="element.id" >
              {{element}}
            </td>
          </tr>
        </tbody>
      </table>
  </div>
  <div v-else>Nenhum item encontrado</div>
</div>
</template> 

<script>
import axios from 'axios';
export default {
  name: "Search",
  data: () => {
    return {
      searching: '',
      column: "RegistroANS",
      answer: 'start'
    }
  },
  methods: {
    getData(){
      axios({
        method: 'GET',
        url: `http://localhost:5000?${this.column}=${this.searching}`,
      }).then((res) => {
        this.answer=res.data;
      })
    }
  }
  }
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.app {
  justify-content: center;
}

.container {
  display: flex;
  justify-content: center;
  gap: 10px;
}
input {
  font-size: 1.2em;
  width: 90vh;
}
.table {
  justify-content: start;
  font-size: 0.7rem;
  margin-left: 1%;
  margin-top: 1%;
  width: 98%;
}

</style>
