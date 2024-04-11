<template>
  <div class="category-products-container">
    <b-navbar toggleable="lg" type="light" class="gradient-nav">
      <b-navbar-brand class="navbar-logo"><router-link to="/home">Shopzee</router-link></b-navbar-brand>
      <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>

      <b-collapse id="nav-collapse" is-nav>
        <b-navbar-nav>
          <b-nav-item  class="nav-item"><router-link to="/user/profile">Profile</router-link></b-nav-item>
        </b-navbar-nav>

        <!-- Right aligned nav items -->
        <b-navbar-nav class="ml-auto">
          

          <b-button variant="secondary" class="login-button" size="sm" @click="logout">Logout</b-button>
        </b-navbar-nav>
      </b-collapse>
    </b-navbar>

    <br>
    <b-row class="text-center" v-if="categories.length > 0">
      <b-col md="12">
        <h3>Categories related to your search:</h3>
      </b-col>
    </b-row>
    <b-row>
      <b-col v-for="cat in categories" :key="cat.id" md="4" class="category-card">
        <b-card
          :title="cat.name"
          :title-tag="'h2'"
          class="category-card-inner"
          tag="article"
          style="font-weight: bold;"
        >

        <div class="category-image-container">
          <img :src="getImageSrc(cat.image)" alt="Category Image" class="category-image" />
        </div>
          <b-card-text class="category-card-text">
            Description:  {{ cat.desc }}
          </b-card-text>
          

          <b-button variant="primary" class="view-products-btn" :to="`/products/${cat.id}`">
            View Products
          </b-button>
        </b-card>
      </b-col>
    
    </b-row>
  </div>
</template>

<script>
import axios from 'axios';
import { mapActions } from 'vuex';


export default{
   
      data() {
        return {
          categories: [],
        };
      },
      mounted() {
        this.getSearched();
        document.title='Search-Category';
      },
      methods: {
        getImageSrc(imageData) {
            return `data:image/png;base64,${imageData}`
        },
        getSearched() {
            let payload = {'query': this.$route.params.keyword, 'type': 'category'}
            axios.post('http://127.0.0.1:5000/search', payload,{
            headers: {
                Authorization: localStorage.getItem('token')
            },
        })
            .then(response=> {
                this.categories=response.data.categories;
            })
          .catch(error=> console.error('error :',error));
        },
        ...mapActions({
            signOut: 'LOGOUT_ACTION'
        }),
      logout(){
        this.signOut()
      }
        
       
      
        
      }
    
}
</script>


<style scoped>
/* General styles */
.category-products-container {
  padding: 0px;
  background-image: url("@/assets/dark.jpg");
  background-size: cover;
  background-position: center;
  min-height: 100vh;
}

.view-products-btn {
  width: 100%;
  margin-top: 10px;
  background-color: #007bff;
}

.view-products-btn a {
  color: white;
  text-decoration: none;
}

.show-card {
  margin: 20px;
}

.category-image-container {
  width: 100%; 
  height: 200px; 
  overflow: hidden;
  display: flex;
  align-items: center;
  justify-content: center;
}

.category-image {
  max-width: 100%;
  max-height: 100%;
}

.gradient-nav {
  background-image: url("@/assets/card.jpeg");
  background-size: cover;
  background-position: center;
  color: white;
}

.category-card-text {
  font-size: 18px;
  color: #000000;
}

.category-card-inner{
  margin: 20px;
}
.navbar-logo {
  font-size: 24px;
  font-weight: bold;
}

.nav-item {
  font-size: 16px;
  /* color: black; */
}

.nav-item a{
  color: black;
  text-decoration: none;
}

/* Search bar styles */
.search-form {
  margin-bottom: 10px;
}

.search-input {
  border-radius: 20px;
  border: none;
  background-color: rgba(255, 255, 255, 0.8);
  padding: 8px 12px;
  color: #333;
}

.search-button {
  border-radius: 20px;
  margin-left: 10px;
  background-color: #007bff;
  color: white;
  font-weight: bold;
}

/* Login button styles */
.login-button {
  border-radius: 20px;
  background-color: #f55;
  color: white;
  font-weight: bold;
}

.login-button a {
  color: white;
  text-decoration: none;
}

/* Show card styles */
.show-card-inner {
  border: none;
  border-radius: 10px;
  box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.3);
  background-image: url("@/assets/blue.jpeg");
  background-size: cover;
  background-position: center;
}

.show-card-text {
  font-size: 14px;
  color: #555;
}

.book-tickets-btn {
  width: 100%;
  margin-top: 10px;
  background-color: #007bff;
}

.book-tickets-btn a {
  color: white;
  text-decoration: none;
}

/* Media queries for responsiveness */
@media screen and (max-width: 767px) {
  .show-card {
    flex: 0 0 100%;
    max-width: 100%;
  }
}
</style>