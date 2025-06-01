  <script setup>
      import { initializeApp } from "firebase/app";
      import { getMessaging, getToken, onMessage } from "firebase/messaging";
      const { login, jwtLogin, logout, user, isAuthenticated } = useAuth()
      const Api = useApi()
      const firebaseConfig = {
        apiKey: "AIzaSyBdG0LUHm6y1GAjhtV8w3KXJ-mLJ7-_Lm4",
        authDomain: "ajkerpristha.firebaseapp.com",
        projectId: "ajkerpristha",
        storageBucket: "ajkerpristha.appspot.com",
        messagingSenderId: "398614736048",
        appId: "1:398614736048:web:c49bdeb58296508bdcdf75",
        measurementId: "G-VWZMRP7HEV"
      };
      const app = initializeApp(firebaseConfig);
  
  
    // Get registration token. Initially this makes a network call, once retrieved
    // subsequent calls to getToken will return from cache.
    const messaging = getMessaging();
    getToken(messaging, { vapidKey: 'BCd57IEhxpEXWtB8P861S4annUYMk9s48C1D5OC9qlxbAorjLt1IDnVGJB6Ip7hSrodZ6ZI2BzT5reEReQaJupk' }).then((currentToken) => {
      if (currentToken) {
        // Send the token to your server and update the UI if necessary
        console.log(user.value.fb_tokens);
        if(isAuthenticated.value && user.value){
          console.log('Token is', isAuthenticated.value,currentToken);
          if(!user.value.fb_tokens.includes(currentToken)){
            console.log('Token not present');
            Api.post('/api/account/fb_tokens/', {token: currentToken}).then((res)=>{
              console.log(res);
            }).catch((err)=>{
              console.log(err);
            })
          }
        }
        // ...
      } else {
        // Show permission request UI
        console.log('No registration token available. Request permission to generate one.');
        // ...
      }
    }).catch((err) => {
      console.log('An error occurred while retrieving token. ', err);
      // ...
    });
  </script>
<template>
    <section></section>
</template>
  
  
  <style scoped>
  </style>