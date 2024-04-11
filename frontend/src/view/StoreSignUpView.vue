<template>
  <div>
    <SignUp />

  </div>
</template>






<script>

// import axios from 'axios'
import SignUp from '../components/StoreSignUp.vue'

export default {
    
    components:{SignUp},
    data() {
      return {
        form: {
          email: '',
          password:'',
          
        },
        show: true
      }
    },
    methods: {
      onSubmit(event) {
        event.preventDefault()
        let payload = {"email":this.form.email, "password":this.form.password}
        console.log(payload)
        // axios.post('http://127.0.0.1:5000/register', payload)
      },
      onReset(event) {
        event.preventDefault()
        // Reset our form values
        this.form.email = ''
        this.form.email = ''
        this.form.password=''
        // Trick to reset/clear native browser form validation state
        this.show = false
        this.$nextTick(() => {
          this.show = true
        })
      }
    }
  }

</script>

<style scoped>
.register input{
    width: 300px;
    height: 40px;
    padding-left: 20px;
    display: block;
    margin-bottom: 30px;
    margin-right: auto;
    margin-left: auto;
    border: 3px solid skyblue;
}



.register button{
    width: 320px;
    height: 40px;
    border: 3px solid black;
    background: skyblue;
    color: black;
    cursor: pointer;
}
</style>
