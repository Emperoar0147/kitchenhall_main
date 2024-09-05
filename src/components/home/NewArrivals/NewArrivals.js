import React from "react";
import Slider from "react-slick";
import Heading from "../Products/Heading";
import Product from "../Products/Product";
import {
  newArrOne,
  newArrTwo,
  newArrThree,
  newArrFour,
  newArrFive,
} from "../../../assets/images/index";
import SampleNextArrow from "./SampleNextArrow";
import SamplePrevArrow from "./SamplePrevArrow";

const NewArrivals = () => {
  const settings = {
    infinite: true,
    speed: 500,
    slidesToShow: 4,
    slidesToScroll: 1,
    nextArrow: <SampleNextArrow />,
    prevArrow: <SamplePrevArrow />,
    responsive: [
      {
        breakpoint: 1025,
        settings: {
          slidesToShow: 3,
          slidesToScroll: 1,
          infinite: true,
        },
      },
      {
        breakpoint: 769,
        settings: {
          slidesToShow: 2,
          slidesToScroll: 2,
          infinite: true,
        },
      },
      {
        breakpoint: 480,
        settings: {
          slidesToShow: 1,
          slidesToScroll: 1,
          infinite: true,
        },
      },
    ],
  };
  return (
    <div className="w-full pb-16">
      <Heading heading="New Arrivals" />
      <Slider {...settings}>
        <div className="px-2">
          <Product
            _id="100001"
            img={newArrOne}
            productName="Microwave"
            price="100.00"
            color="Mixed"
            badge={true}
            des="Revolutionize your kitchen with our latest Microwave!
              Fast, efficient, and sleek, it’s designed to make meal prep effortless and enjoyable.
              Experience the convenience of high-tech cooking with every meal!."
          />
        </div>
        <div className="px-2">
          <Product
            _id="100002"
            img={newArrTwo}
            productName="Cake Mixer"
            price="70.00"
            color="Mixed"
            badge={true}
            des="Elevate your baking with our new Cake Mixer!
             Effortlessly blend, whip, and knead with precision and style.
              Perfect for both novice bakers and seasoned pros,
               it’s your ultimate partner for creating delicious masterpieces."
          />
        </div>
        <div className="px-2">
          <Product
            _id="100003"
            img={newArrThree}
            productName="Air Fryer"
            price="80.00"
            color="Mixed"
            badge={true}
            des="Transform your cooking with our latest Air Fryer!
             Enjoy crispy, golden results with less oil and more flavor.
              Perfect for quick, healthy meals that delight the whole family."
          />
        </div>
        <div className="px-2">
          <Product
            _id="100004"
            img={newArrFour}
            productName="Toaster"
            price="60.00"
            color="Mixed"
            badge={false}
            des="Elevate your breakfast game with our sleek new toaster!
             Enjoy perfectly golden, crispy toast every time with easy-to-use
              settings and a stylish design that complements any kitchen."
          />
        </div>
        <div className="px-2">
          <Product
            _id="100005"
            img={newArrFive}
            productName="Blender"
            price="60.00"
            color="Mixed"
            badge={false}
            des="Blend, chop, and puree with ease!
             Our versatile blender delivers smooth, consistent results every time,
              making it the perfect addition to your kitchen for all your blending needs."
          />
        </div>
      </Slider>
    </div>
  );
};

export default NewArrivals;
