<template>
  <div>      
    <b-navbar toggleable="lg" type="light" variant="dark" class="gradient-nav">
        <b-navbar-brand  class="navbar-logo"><router-link to="/home">Shopzee</router-link></b-navbar-brand>
        <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>
  
        <b-collapse id="nav-collapse" is-nav>
          <b-navbar-nav>
            <b-nav-item class="nav-item"><router-link to="/user/profile">Profile</router-link></b-nav-item>
          </b-navbar-nav>
  
          <!-- Right aligned nav items -->
          <b-navbar-nav class="ml-auto">
            <b-button variant="secondary" class="login-button" @click="logout">Logout</b-button>
          </b-navbar-nav>
        </b-collapse>
      </b-navbar>
        <br>
    <div class="orders-container">
      <h2>Your Orders</h2>
      <b-card v-for="(order, index) in orders" :key="index" class="order-card">
        <b-card-header>
          Order Time: {{ order[0].time }}
        </b-card-header>
        <b-table :items="order" :fields="fields" class="order-table">
          <template v-slot:cell(product)="data">
            {{ data.value }}
          </template>
          <template v-slot:cell(quantity)="data">
            {{ data.value }}
          </template>
          <template v-slot:cell(amount)="data">
            {{ data.value }}
          </template>
        </b-table>
        <div class="total-amount">
        Total Amount: {{ calculateTotalAmount(order) }}
      </div>
      </b-card>
    </div>
  </div>
  </template>
  
  <script>
  import axios from 'axios'
import {mapActions} from 'vuex'


export default{
    
      data() {
        return {
          orders: {},
          fields: ['product', 'quantity', 'amount']
        };
      },
      mounted() {
        this.getOrders();
        document.title='Your Orders';
      },
      methods: {
        ...mapActions({
            signOut: 'LOGOUT_ACTION'
        }),
        calculateTotalAmount(order) {
        return order.reduce((total, product) => total + product.amount, 0).toFixed(2);
        },
        logout(){
          this.signOut()
        },
        getOrders() {
          const user_id = localStorage.getItem('user_id');
          axios.get(`http://127.0.0.1:5000/checkout?user_id=${user_id}`, {
          headers: {
            'Content-Type': 'application/json',
            Authorization: localStorage.getItem('token'),
            },
          })
          .then((response)=> {
              this.orders=response.data.orders;
              console.log(this.orders);
          })
        .catch(error=> alert('Error :',error));
        }
        }
    
}
</script>

  
  <style scoped>
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
  
  .nav-item {
    font-size: 16px;
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

  .cart-button {
  border-radius: 20px;
  border-color: none;
  background-color: rgb(10, 110, 85);
  color: white;
  font-weight: bold;
}

  .orders-container {
    max-width: 800px;
    margin: 0 auto;
  }
  
  .order-card {
    margin-bottom: 20px;
  }
  
  .order-table {
    margin-top: 10px;
  }
  .total-amount {
  font-weight: bold;
  margin-top: 10px; /* Adjust as needed for spacing */
}

  </style>
  