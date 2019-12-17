<template>
  <div class="width">
    <input class="width" type="text" v-model="searchTerm" @click="load">
    <div style="max-height: 200px; overflow-y: scroll;width: 215px;">
      <div @click="clicked(text)" class="list" v-for="(text,idx) in items" :key="idx">{{text}}</div>
    </div>
  </div>
</template>

<script>
  import axios from 'axios';

  export default {
    name: 'Autocomplete',
    data: function () {
      return {
        searchTerm: null,
        show: false,
        items: [],
      };
    },

    watch: {
      searchTerm(v) {
        if (!this.show || !v) 
          this.items = [];
        else {
          axios.get(`${process.env.VUE_APP_API_URL}/items/${v}/`).then(({data}) => {
            this.items = data;
          });
        }
      }
    },
    methods: {
      load() {
        this.show=true;
      },
      clicked(text) {
        this.searchTerm=text;
        this.show=false;
      }
    }
  }
</script>

<style>
.width {
  width: 200px;
}

.list {
  display: block;
  border: 1px solid;
  margin-top: 1px;
}
</style>