package com.itechhub.datawizards.smartcityai.fragments;

import android.os.Bundle;
import android.support.v4.app.Fragment;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;

import com.itechhub.datawizards.smartcityai.R;

public class In_Progress_Citizen extends Fragment {

    public In_Progress_Citizen() {
    }

    @Override
    public void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
    }

    @Override
    public View onCreateView(LayoutInflater inflater, ViewGroup container,
                             Bundle savedInstanceState) {
        // Inflate the layout for this fragment
        View rootView = inflater.inflate(R.layout.in__progress, container, false);

        return rootView;
    }
}
