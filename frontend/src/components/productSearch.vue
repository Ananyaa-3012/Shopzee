<template>
    <div class="pdt-products-container">
      <b-navbar toggleable="lg" type="light" class="gradient-nav">
        <b-navbar-brand class="navbar-logo"><router-link to="/home">Shopzee</router-link></b-navbar-brand>
        <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>
  
        <b-collapse id="nav-collapse" is-nav>
          <b-navbar-nav>
            <b-nav-item  class="nav-item"><router-link >Profile</router-link></b-nav-item>
          </b-navbar-nav>
  
          <!-- Right aligned nav items -->
          <b-navbar-nav class="ml-auto">
            
  
            <b-button variant="secondary" class="login-button" size="sm" @click="logout">Logout</b-button>
          </b-navbar-nav>
        </b-collapse>
      </b-navbar>
      <!-- <div>
    <label for="expiryFilter">Filter by Expiry Date:</label>
    <input type="date" id="expiryFilter" v-model="expiryFilter" @change="applyFilters">

    <label for="priceFilter">Filter by Price:</label>
    <input type="number" id="priceFilter" v-model="priceFilter" @change="applyFilters">
  </div>   -->
      <br>
      <b-row class="text-center" v-if="products.length > 0">
        <b-col md="12">
          <h3>Products related to your search:</h3>
        </b-col>
      </b-row>
      <div v-if="products.length>0">
      <b-row>
        <b-col v-for="pdt in products" :key="pdt.id" md="4" class="pdt-card">
          <b-card
          :title="pdt.name"
          tag="article"
          class="pdt-card-inner"
          :class="{ 'out-of-stock': pdt.stock === 0 }"
        >
        <div class="pdt-image-container">
          <img :src="getImageSrc(pdt.image)" alt="Show Image" class="pdt-image" />
        </div>
          
          <br><br>
          <b-card-text class="pdt-card-text">
            Price: Rs.{{ pdt.price }}
          </b-card-text>
          <b-card-text class="pdt-card-text">
            Manufacturing Date: {{ pdt.manufac }}
          </b-card-text>
          <b-card-text class="pdt-card-text">
            Expiry Date: {{ pdt.expiry }}
          </b-card-text>
          
          <div v-if="pdt.stock === 0" class="out-of-stock-label">Out of Stock</div>

          <b-button 
          variant="primary" 
          class="book-tickets-btn" 
          :to="`/cart/add/${pdt.id}`" 
          :disabled="pdt.stock === 0"
          style="width:50%">

            Add To Cart</b-button>
        </b-card>
        </b-col>
      
      </b-row>
    </div>
    <div v-else>
      <h2>Your search query did not match any results</h2>
      <b-button variant="primary" to="/home" class="keep-shopping">Keep Shopping</b-button>
    </div>
    </div>
  </template>
  
  <script>
  import axios from 'axios';
  import { mapActions } from 'vuex';
  
  
  export default{
     
        data() {
          return {
            products: [],
          };
        },
        mounted() {
          this.getSearched();
        },
        methods: {
          getImageSrc(imageData) {
              return `data:image/png;base64,${imageData}`
          },
          getSearched() {
              let payload = {'query': this.$route.params.keyword, 'type': 'product', 'category':this.$route.params.cat_id}
              axios.post('http://127.0.0.1:5000/search', payload,{
              headers: {
                  Authorization: localStorage.getItem('token')
              },
          })
              .then(response=> {
                  this.products=response.data.products;
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
  .pdt-products-container {
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
  
  .pdt-card {
    margin: 20px;
  }
  
  .pdt-image-container {
    width: 100%; 
    height: 200px; 
    overflow: hidden;
    display: flex;
    align-items: center;
    justify-content: center;
  }
  
  .pdt-image {
    max-width: 100%;
    max-height: 100%;
  }
  .keep-shopping{
    box-align: center; 
    border-radius: 15px; 
    background-color: rgb(10, 110, 85);
    margin: 15px;
  }
  .gradient-nav {
    background-color: white;
    background-size: cover;
    background-position: center;
    color: white;
  }
  
  .pdt-card-text {
    font-size: 18px;
    color: #ffffff;
  }
  
  .pdt-card-inner{
    margin: 20px;
  }
  .navbar-logo {
    font-size: 24px;
    font-weight: bold;
  }
  
  .nav-item {
    font-size: 16px;
  }
  
  .nav-item a{
    color: white;
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
  .pdt-card-inner {
    border: none;
    border-radius: 10px;
    box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.3);
    /* background-image: url("@/assets/blue.jpeg");
    background-size: cover;
    background-position: center; */
  }
  
  .pdt-card-text {
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
    .pdt-card {
      flex: 0 0 100%;
      max-width: 100%;
    }
  }
  </style>