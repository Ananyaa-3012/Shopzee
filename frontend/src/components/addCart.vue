<template>
    <div class="create-category-container">
      <b-card id="category-card">
      <h1>Add to Cart</h1>
      <form @submit.prevent="submitForm" class="category-form">
        
        
        Name: {{ product.name }}<br>
        Expiry Date: {{ product.expiry }}<br>
        Price: {{ product.price }} per {{ product.unit }}
         
        <b-form-group label="Quantity: " label-for="qty">
          <b-form-input type="number" v-model="qty" id="qty" required min="1" :max="product.stock"></b-form-input>
        </b-form-group>

  
        <b-button type="submit" variant="primary">Add To Cart</b-button>
      </form>
    </b-card>
    </div>
  </template>
  
  <script>
  import axios from 'axios';
  export default {
    data() {
      return {
        qty: '',
        product: {
    },

      };
    },
    created() {
    this.getProduct();
    document.title='Add to Cart';
  },
    methods: {
        getProduct() {
            const pdt_id = this.$route.params.pdt_id;
            const apiurl = `http://127.0.0.1:5000/getProduct/${pdt_id}` 
            axios.get(apiurl,{
            headers: {
                Authorization: localStorage.getItem('token'),
            },
        })
            .then(response=> {
                this.product=response.data;
            })
          .catch(error=> console.error('error :',error));
        },
        
        submitForm() {
        const formData = new FormData();
        formData.append('qty', this.qty);
        formData.append('user_id', localStorage.getItem('user_id'));
  
        // Adjust the endpoint and headers based on your API
        const pdt_id = this.$route.params.pdt_id
        const apiurl = `http://127.0.0.1:5000/cart_add/${pdt_id}`;
  
        axios.post(apiurl, formData, {
          headers: {
            'Content-Type': 'application/json',
            Authorization: localStorage.getItem('token'),
          },
        })
        .then((response) => {
          alert(response.data.message);
          this.$router.push(`/products/${this.product.category}`)
        })
        .catch((error) => {
          alert(error);
        });
      },
    },
  };
  </script>
  
  <style scoped>
  .create-category-container {
    display: flex;
    justify-content: center;
    align-items: center;
    margin: 0 auto;
    padding: 50px 20px; /* Adjust padding for smaller screens */
    text-align: center;
    background-image: url("@/assets/dark.jpg");
    background-size: cover;
    background-position: center;
    min-height: 100vh;
  }
  
  .category-card{
    width: 50%;
    align-items: center;
  }
  
  .category-form {
    margin-top: 20px;
  }
  
  .category-form label {
    display: block;
    margin-bottom: 5px;
    font-weight: bold;
  }
  
  .category-form input[type="text"],
  .category-form input[type="number"],
  .category-form input[type="file"] {
    width: 100%;
    padding: 8px;
    margin-bottom: 15px;
    border: 1px solid #ccc;
    border-radius: 5px;
    font-size: 14px;
  }
  
  .submit-button {
    background-color: #007bff;
    color: white;
    border: none;
    padding: 10px 20px;
    border-radius: 5px;
    font-size: 16px;
    cursor: pointer;
  }
  
  .created-category {
    margin-top: 30px;
    text-align: center;
  }
  
  .category-details {
    margin-bottom: 15px;
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
  
  .go-back-button {
    margin-top: 20px;
  }
  </style>
  