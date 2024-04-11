<template>
    <div class="categories-container">
      <b-navbar toggleable="lg" type="light" variant="dark" class="gradient-nav">
        <b-navbar-brand  class="navbar-logo">Shopzee - Admin</b-navbar-brand>
        <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>
  
        <b-collapse id="nav-collapse" is-nav>
  
          <!-- Right aligned nav items -->
          <b-navbar-nav class="ml-auto">
            <b-button variant="secondary" class="login-button" size="sm" @click="logout">Logout</b-button>
          </b-navbar-nav>
        </b-collapse>
      </b-navbar>
        <br>
      <b-row>
        <b-col md="6" class="category-card">
          <b-card 
          title="Category Management"
          :title-tag="'h2'"
          class="category-card-inner"
          tag="article"
          style="font-weight: bold;"
        >

        <b-button variant="primary" to="/admin/category">Show Categories</b-button><br>            
          </b-card>
        </b-col>

        <b-col md="6" class="category-card">
          <b-card 
          title="Approvals"
          :title-tag="'h2'"
          class="category-card-inner"
          tag="article"
          style="font-weight: bold;"
        >

        <b-button variant="primary" style="margin-right:10px;" to="/approval/categories">Category Approvals</b-button>         
        <b-button variant="primary" to="/approval/managers">Store Manager Approvals</b-button>            
          </b-card>
        </b-col>

      </b-row>
    </div>
  </template>
  
  
  <script>
  import axios from 'axios';
  import {mapActions} from 'vuex'
  
  export default {
    data() {
      return {
        categories: [],
        form: {
          searchQuery: ''
        }
      };
    },
    mounted() {
      this.category();
      document.title='Admin Dashboard';
    },
    methods: {
      getImageSrc(imageData) {
              return `data:image/png;base64,${imageData}`
          },
  
      category() {
        axios
          .get('http://127.0.0.1:5000/category',{
              headers: {
                  Authorization: localStorage.getItem('token')
              },
          })
          .then((response) => {
            this.categories = response.data;
             
          })
          .catch((error) => console.error('error:', error));
          
      },
      onSubmit(event) {
          event.preventDefault()
          let url = `/search/${this.form.searchQuery}`;
          console.log(url)
          console.log(this.form.searchQuery)
          // console.log(payload)
          this.$router.push(url);
         
        },
        ...mapActions({
              signOut: 'LOGOUT_ACTION'
          }),
        logout(){
          this.signOut()
        }
      
    }
  };
  </script>
  
  <style scoped>
  /* General styles */
  .categories-container {
    padding: 0px;
    background-image: url("@/assets/dark.jpg");
    background-size: cover;
    background-position: center;
    min-height: 100vh;
  }
  
  .category-card {
    margin-bottom: 20px;
    padding: 0 50px 0 50px;
  }
  
  .gradient-nav {
    background-image: url("@/assets/card.jpeg");
    background-size: cover;
    background-position: center;
    color: white;
  }
  
  .navbar-logo {
    font-size: 24px;
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
  
  
  .category-card-inner {
    border: none;
    border-radius: 10px;
    box-shadow: 0px 8px 16px rgb(0, 0, 0);
    background-image: url("@/assets/card.jpeg");
    background-size: cover;
    font-weight: bold;
    background-position: center;
  }
  
  .category-card-text {
    margin: 10px;
    font-size: 18px;
    color: #000000;
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
  
  
  @media screen and (max-width: 767px) {
    .category-card {
      flex: 0 0 100%;
      max-width: 100%;
    }
  }
  </style>