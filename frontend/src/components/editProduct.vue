<template>
  <div class="create-category-container">
    <b-card id="category-card">
    <h3>Edit Product - {{ product.name }}</h3>
    <form @submit.prevent="submitForm" class="category-form">

      <b-form-group label="Date of Manufacture" label-for="manufac">
        <b-form-input type="date" v-model="product.manufac" id="manufac" required ></b-form-input>
      </b-form-group>

      <b-form-group label="Expiry Date" label-for="expiry">
        <b-form-input type="date" v-model="product.expiry" id="expiry" required ></b-form-input>
      </b-form-group>

      <b-form-group label="Price" label-for="price">
        <b-form-input type="number" v-model="product.price" id="price" required ></b-form-input>
      </b-form-group>

      <b-form-group label="Unit" label-for="unit">
        <b-form-select v-model="product.unit" id="unit" required>
          <option value="Kg">Kg</option>
          <option value="g">g</option>
          <option value="mg">mg</option>
          <option value="l">l</option>
          <option value="ml">ml</option>
          <option value="nos">nos</option>
        </b-form-select>
      </b-form-group>

      <b-form-group label="Stock" label-for="stock" >
        <b-form-input type="number" v-model="product.stock" id="stock" required></b-form-input>
      </b-form-group>

      <b-form-group label="Image" label-for="upload_image">
        <b-form-file v-model="uploadImage" id="upload_image" accept=".jpg, .jpeg, .png" required></b-form-file>
      </b-form-group>

      <b-button type="submit" variant="primary">Submit</b-button>
    </form>
  </b-card>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
  return {
    uploadImage: null,
    product: {
      manufac: '',
      expiry: '',
      price: '',
      unit: '',
      stock: '',
    },
    category: {},
  };
},
  created() {
    this.getProduct();
    document.title='Edit Product';
  },
  methods: {
    handleImageUpload(event) {
      this.uploadImage = event.target.files[0];
    },
    getImageUrl(imageName) {
      return `${imageName}`;
    },

    getProduct() {
            const pdt_id = this.$route.params.pdt_id;
            const apiurl = `http://127.0.0.1:5000/getProduct/${pdt_id}` 
            axios.get(apiurl,{
            headers: {
                Authorization: localStorage.getItem('token')
            },
        })
            .then(response=> {
                this.product=response.data;
            })
          .catch(error=> console.error('error :',error));
        },

    submitForm() {
      const formData = new FormData();
      formData.append('stock', this.product.stock);
      formData.append('manufac', this.product.manufac);
      formData.append('expiry', this.product.expiry);
      formData.append('price', this.product.price);
      formData.append('unit', this.product.unit);
      formData.append('image', this.uploadImage);
      
      console.log(this.stock, this.manufac,this.expiry,this.price,this.unit)
      const cid = this.$route.params.cat_id;
      const pid = this.$route.params.pdt_id;
      const apiurl = `http://127.0.0.1:5000/pdt_update/${cid}/${pid}`;
      axios
        .post(apiurl, formData, {
          headers: {
            'Content-Type': 'multipart/form-data',
            Authorization: localStorage.getItem('token')
          },
        })
        .then(() => {
          alert("Product updated successfully");
          this.$router.push(`/store/products/${cid}`)
        })
        .catch((error) => {
          console.error(error);
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
