import React from "react";
import Heading from "../Products/Heading";
import Product from "../Products/Product";
import {
  bestSellerOne,
  bestSellerTwo,
  bestSellerThree,
  bestSellerFour,
} from "../../../assets/images/index";

const BestSellers = () => {
  return (
    <div className="w-full pb-20">
      <Heading heading="Our Bestsellers" />
      <div className="w-full grid grid-cols-1 md:grid-cols-2 lgl:grid-cols-3 xl:grid-cols-4 gap-10">
        <Product
          _id="1011"
          img={bestSellerOne}
          productName="Air Fryer"
          price="70.00"
          color="mixed"
          badge={true}
          des="Experience the crunch without the guilt—our best-selling Air Fryer
           transforms your favorite foods into crispy delights with a fraction of the oil!"
        />
        <Product
          _id="1012"
          img={bestSellerTwo}
          productName="Baking Wares"
          price="60.00"
          color="Mixed"
          badge={false}
          des="Elevate your baking game with our best-selling baking wares—precision tools
           for creating flawless cakes, cookies, and more!"
        />
        <Product
          _id="1013"
          img={bestSellerThree}
          productName="Kitchen Utensils"
          price="45.00"
          color="Mixed"
          badge={true}
          des="Discover our top kitchen utensils—your secret to effortless
           cooking and perfect results every time!"
        />
        <Product
          _id="1014"
          img={bestSellerFour}
          productName="Set of Pots"
          price="90.00"
          color="Mixed"
          badge={false}
          des="Elevate your cooking with our premium set of pots—designed
           for delicious meals and lasting performance!"
        />
      </div>
    </div>
  );
};

export default BestSellers;
