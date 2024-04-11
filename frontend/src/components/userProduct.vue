<template>
  <div class="category-products-container">
    <b-navbar toggleable="lg" type="danger" variant="info" class="gradient-nav">
      <b-navbar-brand  class="navbar-logo"><router-link to="/home">Shopzee</router-link></b-navbar-brand>
      <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>

      <b-collapse id="nav-collapse" is-nav>

        <!-- Right aligned nav items -->
        <b-navbar-nav class="ml-auto">
          <b-nav-form @submit="onSubmit">
            <b-form-input v-model="form.query" size="sm" class="search-input" placeholder="Search" :disabled="products.length === 0"></b-form-input>
            <b-button  class="search-button" type="submit" :disabled="products.length === 0">Search</b-button>
          </b-nav-form>
          <b-button class="cart-button" variant="primary" to="/cart">Cart</b-button>
          <b-button variant="secondary" class="login-button"  @click="logout">Logout</b-button>
        </b-navbar-nav>
      </b-collapse>
    </b-navbar>

    <br>
    <div v-if="products.length>0">
    <b-row >
      <b-col v-for="pdt in products" :key="pdt.id" class="show-card" cols="3">
        <b-card
          :title="pdt.name"
          tag="article"
          class="show-card-inner"
          :class="{ 'out-of-stock': pdt.stock === 0 }"
        >
        <div class="show-image-container">
          <img :src="getImageSrc(pdt.image)" alt="Show Image" class="show-image" />
        </div>
          
          <br><br>
          <b-card-text class="category-card-text">
            Price: Rs.{{ pdt.price }}
          </b-card-text>
          <b-card-text class="category-card-text">
            Manufacturing Date: {{ pdt.manufac }}
          </b-card-text>
          <b-card-text class="category-card-text">
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
    <h2>No products in this category</h2>
    <b-button to="/home" class="cart-button">Keep Shopping</b-button>
  </div>
  </div>
</template>


<script>
import axios from 'axios'
import {mapActions} from 'vuex'


export default{
    
      data() {
        return {
          products: {},
          form: {
            query: ''
        },
        cat_id:0
        };
      },
      created() {
        this.cat_id = this.$route.params.cat_id;
        this.getProducts();
        this.getCart();
        document.title='Products'
      },
      methods: {
        getImageSrc(imageData) {
            return `data:image/png;base64,${imageData}`
        },
        ...mapActions({
            signOut: 'LOGOUT_ACTION'
        }),
      logout(){
        this.signOut()
      },
        getProducts() {
            const apiurl = `http://127.0.0.1:5000/pdt_view/${this.cat_id}` 
            axios.get(apiurl,{
            headers: {
                Authorization: localStorage.getItem('token')
            },
        })
            .then(response=> {
                this.products=response.data;
            })
          .catch(error=> console.error('error :',error));
        },
      onSubmit(event) {
        event.preventDefault()
        let url = `/search/${this.cat_id}/${this.form.query}`;
        this.$router.push(url);
       
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



.show-card {
  margin: 20px;
}

.category-card-text {
  font-size: 18px;
  color: #000000;
}

.show-image-container {
  width: 100%; 
  height: 200px; 
  overflow: hidden;
  display: flex;
  align-items: center;
  justify-content: center;
}

.show-image {
  max-width: 100%;
  max-height: 100%;
}

.show-card-text {
  font-size: 20px;
  color: #ffffff;
}

.gradient-nav {
  background-image: url("@/assets/card.jpeg");
  background-size: cover;
  background-position: center;
  color: rgb(0, 0, 0);
}

.navbar-logo {
  font-size: 24px;
  font-weight: bold;
}

.nav-item a{
  color: black;
  text-decoration: none;
}

.nav-item {
  font-size: 16px;
}

/* Search bar styles */
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

.cart-button {
  border-radius: 20px;
  border-color: none;
  background-color: rgb(10, 110, 85);
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
  background-image: url("@/assets/card.jpeg");
  background-size: cover;
  background-position: center;
}

.out-of-stock {
  opacity: 0.7; /* Dim the product */
  pointer-events: none; /* Disable pointer events for the product */
  border: 2px solid red;
}

.out-of-stock-label {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  font-size: 18px;
  font-weight: bold;
  color: red;
}
.show-card-text {
  font-size: 14px;
  color: #000000;
}

.book-tickets-btn {
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