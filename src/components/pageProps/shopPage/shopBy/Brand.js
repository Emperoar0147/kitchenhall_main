import React, { useState } from "react";
import { motion } from "framer-motion";
import NavTitle from "./NavTitle";
import { useDispatch, useSelector } from "react-redux";
import { toggleBrand } from "../../../../redux/kitchenhallSlice";

const Brand = () => {
  const [showBrands, setShowBrands] = useState(true);
  const checkedBrands = useSelector(
    (state) => state.orebiReducer.checkedBrands
  );
  const dispatch = useDispatch();

  const brands = [
    {
      _id: 900,
      title: "LG",
    },
    {
      _id: 901,
      title: "Bosch",
    },
    {
      _id: 902,
      title: "samsung",
    },

    {
      _id: 903,
      title: "Whirlpool",
    },

    {
      _id: 904,
      title: "GE",
    },

    {
      _id: 905,
      title: "Frigidaire",
    },

    {
      _id: 906,
      title: "KitchenAid",
    },

    {
      _id: 907,
      title: "Miele",
    },

    {
      _id: 908,
      title: "Beko",
    },

    {
      _id: 909,
      title: "Maytag",
    },

    {
      _id: 910,
      title: "Electrolux",
    },

    {
      _id: 911,
      title: "Panasonic",
    },

    {
      _id: 912,
      title: "Amana",
    },

    {
      _id: 913,
      title: "Gaggenau",
    },

    {
      _id: 914,
      title: "Haire",
    },

    {
      _id: 915,
      title: "Hotpoint",
    },

    {
      _id: 916,
      title: "Thermodore",
    },

    {
      _id: 917,
      title: "Viking",
    },

    {
      _id: 918,
      title: "Bertazzoni",
    },

    {
      _id: 919,
      title: "Dacor",
    },

    {
      _id: 920,
      title: "Fisher & Paykel",
    },

    {
      _id: 921,
      title: "jennAir",
    },

    {
      _id: 922,
      title: "Kenmore",
    },

    {
      _id: 923,
      title: "ASKO",
    },
  ];

  const handleToggleBrand = (brand) => {
    dispatch(toggleBrand(brand));
  };

  return (
    <div>
      <div
        onClick={() => setShowBrands(!showBrands)}
        className="cursor-pointer"
      >
        <NavTitle title="Shop by Brand" icons={true} />
      </div>
      {showBrands && (
        <motion.div
          initial={{ y: -20, opacity: 0 }}
          animate={{ y: 0, opacity: 1 }}
          transition={{ duration: 0.5 }}
        >
          <ul className="flex flex-col gap-4 text-sm lg:text-base text-[#767676]">
            {brands.map((item) => (
              <li
                key={item._id}
                className="border-b-[1px] border-b-[#F0F0F0] pb-2 flex items-center gap-2 hover:text-primeColor hover:border-gray-400 duration-300"
              >
                <input
                  type="checkbox"
                  id={item._id}
                  checked={checkedBrands.some((b) => b._id === item._id)}
                  onChange={() => handleToggleBrand(item)}
                />
                {item.title}
              </li>
            ))}
          </ul>
        </motion.div>
      )}
    </div>
  );
};

export default Brand;
