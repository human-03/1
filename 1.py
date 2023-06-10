print("hi")
package com.app.login_app;
import javax.servlet.http.HttpSession;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.data.jpa.repository.Modifying;
import org.springframework.data.jpa.repository.Query;
import org.springframework.data.repository.query.Param;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestMapping;

@Controller
public class RegistrationController {

    @Autowired
    private UserRepository userRepository;

    @RequestMapping("/register")
    public String showregisterPage(Model model) {
        model.addAttribute("errorMessage", "");
        return "register";
    }

    @PostMapping("/register")
    public String register(String username, String password, HttpSession session, Model model) {
        User user = userRepository.findByUsername(username);

        if (user != null  && user.getUsername().equals(username)) {
            model.addAttribute("errorMessage", "The username is already in use!");
            return "register";
        }
//        @Modifying
//        @Query(value="INSERT INTO user_details(username,password) VALUES(username,password)",nativeQuery=true)
//        @Query("insert into User (name, email) values (:name, :email)")
//        void insertUser(@Param("name") String name, @Param("email") String email);
//        
        return "redirect:/login";
    }
}